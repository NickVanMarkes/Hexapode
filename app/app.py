from flask import Flask, render_template,Response, request
import os
import time
import random
from turbo_flask import Turbo
import threading
import cv2
import numpy as np
from sense_hat import SenseHat
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from threading import Timer

# Mes Classes
from mod_classes.Camera import VideoCamera
from mod_classes.Lidar import Lidar

app = Flask(__name__)
turbo = Turbo(app)
sense = SenseHat()


#Constantes
X = [255, 0, 0]  # Red
Z = [0, 255, 0]  # Green
Y = [0, 0, 255]  # Green
A = [0,255,255]
O = [0, 0, 0]  # OFF

DMAX = 2000
IMIN = 0
IMAX = 50
# Plot
fig=None
line=None
scans=None

Fleche = [
O, O, O, X, X, O, O, O,
O, O, X, X, X, X, O, O,
O, X, X, X, X, X, X, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O
]

Fleche_G = [
O, O, O, O, O, O, O, O,
O, O, Z, O, O, O, O, O,
O, Z, Z, O, O, O, O, O,
Z, Z, Z, Z, Z, Z, Z, Z,
Z, Z, Z, Z, Z, Z, Z, Z,
O, Z, Z, O, O, O, O, O,
O, O, Z, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

Fleche_D = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, Y, O, O,
O, O, O, O, O, Y, Y, O,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
O, O, O, O, O, Y, Y, O,
O, O, O, O, O, Y, O, O,
O, O, O, O, O, O, O, O
]

Fleche_AH = [
O, O, O, O, O, O, O, O,
O, O, O, A, A, A, A, O,
O, O, A, O, O, O, O, A,
O, A, A, O, O, O, O, O,
O, A, O, O, A, A, A, A,
O, A, A, O, O, O, A, A,
O, O, A, A, A, A, O, A,
O, O, O, O, O, O, O, A
]

Fleche_H = [
O, O, O, O, O, O, O, O,
O, O, A, A, A, A, O, O,
O, A, A, O, O, A, A, O,
O, O, O, O, O, O, A, O,
O, A, A, A, O, O, A, O,
O, A, A, O, O, A, O, O,
O, A, O, A, A, A, O, O,
O, A, O, O, A, O, O, O
]

clean_LED = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

sense.set_pixels(clean_LED)




_incr=0
_angleX=0
_angleY=0 
_angleZ=0
_vitesse=0
_batterie=0 
_batterieServo=0
_obstacleDist=0




# Fonction permettant de générer les images de la caméra.
def generate_frames(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



# Fonction permettant d'actualiser les valeurs
@app.context_processor
def inject_load():
    _angleX=random.randrange(0,360)
    _angleY=random.randrange(0,360)
    _angleZ=random.randrange(0,360)
    _vitesse=random.randrange(0,20)
    _obstacleDist=random.randrange(15,100)
    _batterie=random.randrange(0,100)
    _batterieServo=random.randrange(0,100)
    _incr=random.randrange(0,100000)
    

    return {'angleX': _angleX, 'angleZ': _angleZ, 'angleY': _angleY, "vitesse":_vitesse,
    "batterie":_batterie,"batterieServo":_batterieServo,
    "obstacleDist": _obstacleDist, "increment_plot": _incr}


# Fonction permettant de lancer le rafraîchissement de la page
@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

# Fonction permettant de rafraîchir le site.
def update_load():
    with app.app_context():
        i=0
        while True:
            time.sleep(1)
            i+=1 
            turbo.push(turbo.replace(render_template('index_update.html'), 'load'))
            if i == 3:
                lst_push=[(turbo.replace(render_template('update_plot.html'), 'plotdiv')),(turbo.replace(render_template('index_update.html'), 'load'))]
                turbo.push(lst_push)
                i=0


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
            sense.set_pixels(Fleche)
            pass
        elif request.form['submit_button'] == 'Recule':
            sense.set_pixels(clean_LED)
            pass
        elif request.form['submit_button'] == 'Droite':
            sense.set_pixels(Fleche_D)
            pass
        elif request.form['submit_button'] == 'Gauche':
            sense.set_pixels(Fleche_G)
            pass
        elif request.form['submit_button'] == 'Rotation_AntiHoraire':
            sense.set_pixels(Fleche_AH)
            pass
        elif request.form['submit_button'] == 'Rotation_Horaire':
            sense.set_pixels(Fleche_H)
            pass
        else:
            pass # unknown

@app.route('/plot')
def radar():
    lidar.run()
    
    scans=lidar.Get_Scans()

    for scan in scans:
        offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
        line.set_offsets(offsets)
        intens = np.array([meas[0] for meas in scan])
        line.set_array(intens)

    buf= io.BytesIO()
    FigureCanvas(fig).print_png(buf)

    return Response(buf.getvalue(),mimetype='image/png')

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
    app.run(debug=False, host='0.0.0.0')
    