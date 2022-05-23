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

import math
import threading

# Mes Classes
from mod_classes.Camera import VideoCamera
from mod_classes.LidarAsync import Lidarasync
from mod_classes.RepeatTimer import RepeatTimer
from mod_classes.Plot import Radar
from mod_classes.Gyroscope import Gyroscope
from mod_classes.Animations_Hexapode import Animations

app = Flask(__name__)
turbo = Turbo(app)

mode="controle"
NBSCANS=2
resultwithoutdoubles=[]

#Header
@app.after_request
def add_header(r):
    """      brief       : Fonction executée après chaque requête.
             param-type  : request
             return-type : request
    """ 

    r.headers["Cache-Control"]="no-cache, no-store, must-revalidate"
    r.headers["Pragma"]="no-cache"
    r.headers["Expires"]="0"
    r.headers["Cache-Control"]='public, max-age=0'
    return r

#Rafraichissement Flask
@app.context_processor
def inject_load():
    """      brief       : Fonction permettant d'actualiser les valeurs sur la bannière
             param-type  : None
             return-type : dict[string, Any]
    """ 
    global mode

    if lidar.ShorterScan!= None:
        _obstacleDist=lidar.ShorterScan

    angles=gyroscope.get_angle()
    

    _angleX=round(angles["x"],2)
    _angleY=round(angles["y"],2)
    _angleZ=round(angles["z"],2)
    
    #Vitesse
    #accel=gyroscope.get_acceleration()
    # vx=0
    # vy=0
    # vz=0

    # vx+=accel["x"]*1
    # vy+=accel["y"]*1
    # vz+=accel["z"]*1
    # _vitesse=math.sqrt(vx**2+vy**2+vz**2)

    _batterie=random.randrange(0,100)
    _batterieServo=random.randrange(0,100)


    return {'angleX': _angleX, 'angleZ': _angleZ, 'angleY': _angleY, "batterie":_batterie,
    "batterieServo":_batterieServo,"obstacleDist": _obstacleDist,"mode":mode}



@app.before_first_request
def before_first_request():
    """      brief       : Fonction permettant de lancer le rafraîchissement de la page sur un thread.
             param-type  : None
             return-type : None
    """ 
    threading.Thread(target=update_load).start()


def update_load():
    """      brief       : Fonction permettant de rafraîchir le site.
             param-type  : None
             return-type : None
    """ 
    with app.app_context():
        while True:
            time.sleep(1.0)
            turbo.push(turbo.replace(render_template('index_update.html'), 'load'))

#Home
@app.route('/', methods=['GET', 'POST'])
def index():
    """      brief       : Route principale du site web.
             param-type  : None
             return-type : string
    """ 

    global mode
    print(mode)
    if request.method=="POST":
        if request.form['select-mode']=="controle":
            print('controle ',0)
            mode="controle"
            mouvement()
        elif request.form['select-mode']=="auto":
            print('auto ', 1)
            mode="auto"
        elif request.form['select-mode']=="suiveur":
            print('follow ', 2)
            mode="suiveur"
    thread=threading.Thread(target=anim.Init2)
    thread.start()
    thread.join(anim.Maintiens)
    return render_template('index.html')




#Camera
def generate_frames(camera):
    """      brief       : Fonction permettant de générer les images de la caméra.
             param-type  : VideoCamera
             return-type : bytes
    """ 
    global resultwithoutdoubles
    while True:
        frame=camera.get_frame(resultwithoutdoubles)
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    """      brief       : Route qui affiche le retour de la caméra.
             param-type  : None
             return-type : Response
    """ 
    return Response(generate_frames(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

#Mouvements
def mouvement():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Avance':
            threading.Thread(target=anim.Avance).start()
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

#Radar
def radar():
    """      brief       : Fonction récupère les données du lidar, et enlève les doublons.
             param-type  : None
             return-type : list(list(float,float,float))
    """ 
    global lidar
    global resultwithoutdoubles
    resultwithoutdoubles=[]
    result=lidar.Get_Data()
    while len(resultwithoutdoubles)<NBSCANS:

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
    """      brief       : Fonction permettant de générer la vue radar.
             param-type  : Radar
             return-type : bytes
    """ 
    while True:
        radar()
        frame=radarparam.CreatePlot(radar())
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/plot')
def plot():
    """      brief       : Route qui affiche la vue radar.
             param-type  : None
             return-type : Response
    """ 
    return Response(generate_radar(radar_view),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    radar_view=Radar()
    lidar=Lidarasync()
    lidar.StartLidar()
    gyroscope=Gyroscope()
    threadLidar=RepeatTimer(0.05,lidar.DoScan).start()
    anim=Animations(gyroscope)
    app.run(debug=False, host='0.0.0.0')