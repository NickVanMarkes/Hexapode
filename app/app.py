### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/app.py
### Date        : 04/04/2022
### Description : Programme principal qui récupère toutes les données et les affiches sur un site web et qui servira a contrôler le robot hexapode.


# FLASK
from flask import Flask, render_template,Response, request
from turbo_flask import Turbo
import time
import random

import threading
import cv2
import numpy as np
import io
from threading import Timer

# Matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Mes Classes
from mod_classes.Camera import VideoCamera
from app.mod_classes.Lidarv1 import Lidar

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
Onload=False
array_scans=[]
wait4seconds=0



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

    #Get Obstacles distances
    global array_scans
    global _obstacleDist
    distances=[]
    if scans != None:
        array_scans=scans.copy()
        for scan in array_scans:
            for meas in scan:
                distances.append(meas[2])
    #Set Obstacles distances
    if distances.__len__()!=0:
        distances=sorted(distances)
        _obstacleDist=distances[0]

    _angleX=random.randrange(0,360)
    _angleY=random.randrange(0,360)
    _angleZ=random.randrange(0,360)
    _vitesse=random.randrange(0,20)
    
    _batterie=random.randrange(0,100)
    _batterieServo=random.randrange(0,100)
    wait4seconds+=1
    if wait4seconds==4:
        _incr+=1
        wait4seconds=0
        if _incr > 0:
            memo_incr=_incr-1
    

    return {'angleX': _angleX, 'angleZ': _angleZ, 'angleY': _angleY, "vitesse":_vitesse,
    "batterie":_batterie,"batterieServo":_batterieServo,
    "obstacleDist": _obstacleDist, "increment_plot": _incr, "memo_increment": memo_incr}


# Fonction permettant de lancer le rafraîchissement de la page
@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

# Fonction permettant de rafraîchir le site.
def update_load():
    with app.app_context():
        i=0
        while True:
            time.sleep(1.0)
            i+=1
            if i==4:
                lst_push=[(turbo.replace(render_template('update_plot.html'), 'plotdiv')),(turbo.replace(render_template('index_update.html'), 'load'))]
                turbo.push(lst_push)
                i=0
            else:
                turbo.push(turbo.replace(render_template('index_update.html'), 'load'))



# Route principale
@app.route('/', methods=['GET', 'POST'])
def index():
    mouvement()
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



@app.route('/plot', methods=['GET', 'POST'])
def radar():
    global Onload
    global lidar
    global scans
    if not Onload:
        Onload=True
        lidar.run()

        scans=lidar.Get_Scans()
        for scan in scans:
            offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
            line.set_offsets(offsets)
            intens = np.array([meas[0] for meas in scan])
            line.set_array(intens)

        buf= io.BytesIO()

        FigureCanvas(fig).print_png(buf)
        #fig.savefig("static/img/plot.png")

        Onload=False
        return Response(buf.getvalue(),mimetype='image/png')
    else:
        time.sleep(1)        
        return radar() 
    #return '<img src="data:image/png;base64,{}">'.format(plot_url)
def InitFig():
    #INIT matplotlib
    plt.ion()
    fig = plt.figure(figsize=(3,3))
    return fig

def InitLine():
    #INIT matplotlib
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],
                           cmap=plt.cm.jet, lw=0)
    ax.set_rmax(DMAX)
    ax.grid(True)
    return line

if __name__ == '__main__':
    fig=InitFig()
    line=InitLine()
    lidar=Lidar()
    Onload=False
    app.run(debug=False, host='0.0.0.0')