### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/app.py
### Date        : 04/04/2022
### Description : Programme principal qui récupère toutes les données et les affiches sur un site web et qui servira a contrôler le robot hexapode.


# FLASK
import math
from flask import Flask, render_template,Response, request
from turbo_flask import Turbo
import time
import random

import threading
import numpy as np
import io
from threading import Timer

# Mes Classes
from mod_classes.Camera import VideoCamera
from mod_classes.LidarAsync import Lidarasync
from mod_classes.RepeatTimer import RepeatTimer
from mod_classes.Plot import Radar
from mod_classes.Gyroscope import Gyroscope

app = Flask(__name__)
turbo = Turbo(app)

DMAX = 2000
IMIN = 0
IMAX = 50
# Plot
fig=None
line=None
scans=None

_incr=0
memo_incr=0
_angleX=0
_angleY=0
_angleZ=0
_vitesse=0
_batterie=0
_batterieServo=0
_obstacleDist=0
wait4seconds=0
mode=""


# Fonction permettant de générer les images de la caméra.
def generate_frames(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')





@app.after_request
def add_header(r):
    r.headers["Cache-Control"]="no-cache, no-store, must-revalidate"
    r.headers["Pragma"]="no-cache"
    r.headers["Expires"]="0"
    r.headers["Cache-Control"]='public, max-age=0'
    return r



# Fonction permettant d'actualiser les valeurs
@app.context_processor
def inject_load():
    global _incr
    global memo_incr
    global wait4seconds
    global _obstacleDist
    global mode

    if lidar.ShorterScan!= None:
        _obstacleDist=lidar.ShorterScan

    angles=gyroscope.get_angle()
    accel=gyroscope.get_acceleration()

    _angleX=round(angles["x"],2)
    _angleY=round(angles["y"],2)
    _angleZ=round(angles["z"],2)
    vx=0
    vy=0
    vz=0

    vx+=accel["x"]*1
    vy+=accel["y"]*1
    vz+=accel["z"]*1
    _vitesse=math.sqrt(vx**2+vy**2+vz**2)
    # print(_vitesse)

    _batterie=random.randrange(0,100)
    _batterieServo=random.randrange(0,100)
    wait4seconds+=1
    if wait4seconds==4:
        _incr+=1
        wait4seconds=0
        if _incr > 0:
            memo_incr=_incr-1


    return {'angleX': _angleX, 'angleZ': _angleZ, 'angleY': _angleY, "vitesse":_vitesse,
    "batterie":_batterie,"batterieServo":_batterieServo,"obstacleDist": _obstacleDist,"mode":mode}


# Fonction permettant de lancer le rafraîchissement de la page
@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

# Fonction permettant de rafraîchir le site.
def update_load():
    with app.app_context():
        while True:
            time.sleep(1.0)
            turbo.push(turbo.replace(render_template('index_update.html'), 'load'))


@app.route('/post/<int:id>')
def show_post(id):
    # Shows the post with given id.
    return f'This post has the id {id}'


# Route principale
@app.route('/', methods=['GET', 'POST'])
def index():
    global mode
    print(mode)
    if request.method=="POST":
        if request.form['select-mode']=="1":
            print('controle ',0)
            mode="controle"
            #mode=Controle
            #mouvement()
        elif request.form['select-mode']=="2":
            print('auto ', 1)
            mode="auto"
            #mode=autonome
        elif request.form['select-mode']=="3":
            print('follow ', 2)
            mode="suiveur"
            #mode=suiveur
    return render_template('index.html')

# Route qui affiche le retour de la caméra
@app.route('/video')
def video():
    return Response(generate_frames(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

def mouvement():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Avance':
            #sense.set_pixels(Fleche)
            pass
        elif request.form['submit_button'] == 'Recule':
            #sense.set_pixels(clean_LED)
            pass
        elif request.form['submit_button'] == 'Droite':
            #sense.set_pixels(Fleche_D)
            pass
        elif request.form['submit_button'] == 'Gauche':
            #sense.set_pixels(Fleche_G)
            pass
        elif request.form['submit_button'] == 'Rotation_AntiHoraire':
            #sense.set_pixels(Fleche_AH)
            pass
        elif request.form['submit_button'] == 'Rotation_Horaire':
            #sense.set_pixels(Fleche_H)
            pass
        else:
            pass # unknown




def radar():
    global lidar
    resultwithoutdoubles=[]
    result=lidar.Get_Data()
    while len(resultwithoutdoubles)<2:

     #Ajout des valeurs dans notre liste
        if(result!=lidar.Get_Data()):
            result+=lidar.Get_Data().copy()
    #Retire les doublons
        for scans in result:
            if scans not in resultwithoutdoubles:
                resultwithoutdoubles.append(scans)
        time.sleep(0.05) #Attendre 0.05 secondes
    return resultwithoutdoubles

def generate_radar(radarparam):
    while True:
        radar()
        frame=radarparam.CreatePlot(radar())
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/plot')
def plot():
    return Response(generate_radar(radar_view),mimetype='multipart/x-mixed-replace; boundary=frame')

    #return '<img src="data:image/png;base64,{}">'.format(plot_url)

if __name__ == '__main__':
    radar_view=Radar()
    lidar=Lidarasync()
    lidar.StartLidar()
    gyroscope=Gyroscope()
    threadLidar=RepeatTimer(0.05,lidar.DoScan).start()
    app.run(debug=False, host='0.0.0.0')