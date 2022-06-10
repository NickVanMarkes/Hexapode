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
import subprocess

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
    """  brief: Fonction executée après chaque requête.
             
             parameters  :
                 request  
             
             returns :
                request
        """  

    r.headers["Cache-Control"]="no-cache, no-store, must-revalidate"
    r.headers["Pragma"]="no-cache"
    r.headers["Expires"]="0"
    r.headers["Cache-Control"]='public, max-age=0'
    return r

#Rafraichissement Flask
@app.context_processor
def inject_load():
    """  brief: Fonction permettant d'actualiser les valeurs sur la bannière.
             
             parameters  :
                 None 
             
             returns :
                dict[string, Any]
        """ 
    global mode

    if lidar.ShorterScan!= None:
        _obstacleDist=lidar.ShorterScan

    angles=gyroscope.get_angle()
    

    _angleX=round(angles["x"],2)
    _angleY=round(angles["y"],2)
    _angleZ=round(angles["z"],2)
    
    #Vitesse
    ## Récupération des données de l'accéléromètre
    #accel=gyroscope.get_acceleration()
    # vx=0
    # vy=0
    # vz=0

    ## Calcul de la vitesse
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
    """  brief: Fonction permettant de lancer le rafraîchissement de la page sur un thread.
             
             parameters  :
                 None 
             
             returns :
                None
        """  
    RepeatTimer(1, update_load).start()


def update_load():
    """  brief: Fonction permettant de rafraîchir le site.
             
             parameters  :
                 None 
             
             returns :
                None
        """ 
    with app.app_context():
        turbo.push(turbo.replace(render_template('index_update.html'), 'load'))

#Home
@app.route('/', methods=['GET', 'POST'])
def index():
    """  brief: Route principale du site web.
             
             parameters  :
                 None 
             
             returns :
                string
        """ 

    global mode
    print(mode)
    if request.method=="POST":
        print(request.form['submit_button'])
        if request.form['Select_Modes']=="controle" or (request.form['submit_button']== 'Avance' or request.form['submit_button']== 'Gauche' or request.form['submit_button']== 'Droite' or request.form['submit_button']== 'Recule' or request.form['submit_button']== 'Rotation_Horaire' or request.form['submit_button']== 'Rotation_AntiHoraire' or request.form['submit_button']== 'Init'):
            print('controle ',0)
            mode="controle"
            mouvement()
        elif request.form['Select_Modes']=="auto":
            print('auto ', 1)
            mode="auto"
        elif request.form['Select_Modes']=="suiveur":
            print('follow ', 2)
            mode="suiveur"

        elif request.form['Select_Modes']=="Shut_Down":
            lidar.StopLidar()
            anim.Off()
            subprocess.call(["sudo", "shutdown", "-h", "now"])
    # thread=threading.Thread(target=anim.Init2)
    # thread.start()
    # thread.join(anim.Maintiens)
    return render_template('index.html')




#Camera
def generate_frames(camera):
    """  brief: Fonction permettant de générer les images de la caméra.
             
             parameters  :
                 VideoCamera 
             
             returns :
                bytes
        """
    global resultwithoutdoubles
    while True:
        if mode=="suiveur":
            camera.QRCodeActivated=True
        else:
            camera.QRCodeActivated=False
        frame=camera.get_frame(resultwithoutdoubles)
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    """  brief: Route qui affiche le retour de la caméra.
             
             parameters  :
                 None
             
             returns :
                Response
        """ 
    return Response(generate_frames(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

#Mouvements
def mouvement():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Avance':
            # threading.Thread(target=anim.Avance).start()
            print("Avance")
            anim.Avance()
        elif request.form['submit_button'] == 'Recule':
            #sense.set_pixels(clean_LED)
            print("Recule")
            anim.Recule()
        elif request.form['submit_button'] == 'Droite':
            #sense.set_pixels(Fleche_D)
            print("Droite")
            anim.Droite()
        elif request.form['submit_button'] == 'Gauche':
            #sense.set_pixels(Fleche_G)
            print("Gauche")
            anim.Gauche()
        elif request.form['submit_button'] == 'Rotation_AntiHoraire':
            #sense.set_pixels(Fleche_AH)
            print("Rotation_AntiHoraire")
            anim.Rotation_AntiHoraire()
        elif request.form['submit_button'] == 'Rotation_Horaire':
            #sense.set_pixels(Fleche_H)
            print("Rotation_Horaire")
            anim.Rotation_Horaire()
        elif request.form['submit_button'] == 'Init':
            print("Init")
            anim.Init2()
        else:
            pass # unknown
def mouvement_auto():
    bloque=False
    global resultwithoutdoubles
    if mode=="auto":
        if resultwithoutdoubles!=None:
            for scan in resultwithoutdoubles:
                for meas in scan:
                    # Si l'angle est en face du robot
                    if meas[1]>327 and meas[1]<31 and bloque==False:
                        # Si la distance est inférieur à 5 cm
                        if meas[2]<50:
                            # Bloque le robot
                            bloque=True
                            anim.Maintiens()
                            print("bloque")
                        else:
                            # Continue à avancer
                            print("avance")
                            anim.Avance()
                    # s'il est bloqué
                    if bloque:
                        #Verifie à droite s'il y a un obstacle    
                        if meas[1]>31 and meas[1]<121 and meas[2]>50:
                            print("droite")
                            bloque=False
                            anim.Rotation_Horaire()
                        #Verifie à gauche s'il y a un obstacle
                        elif meas[1]>327 and meas[1]<237 and meas[2]>50:
                            print("gauche")
                            bloque=False
                            anim.Rotation_AntiHoraire()
                        # Sinon il recule
                        else:
                            bloque=False
                            print("recule")
                            anim.Recule()
                        
                        

#Radar
def radar():
    """  brief: Fonction récupère les données du lidar, et enlève les doublons.
             
             parameters  :
                 None
             
             returns :
                list(list(float,float,float))
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
    return resultwithoutdoubles

def generate_radar(radarparam):
    """  brief: Fonction permettant de générer la vue radar.
             
             parameters  :
                 Radar
             
             returns :
                bytes
        """
    while True:
        radar()
        frame=radarparam.CreatePlot(radar())
        yield(b'--frame\r\n'
                   b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

@app.route('/plot')
def plot():
    """  brief: Route qui affiche la vue radar.
             
             parameters  :
                 None
             
             returns :
                Response
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