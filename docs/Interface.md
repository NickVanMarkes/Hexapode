# Interface Web
````html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Interface_FlaskV3</title>
    <link rel="stylesheet" href="static/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto&amp;display=swap">
    <link rel="stylesheet" href="static/css/styles.css">
    <link rel="stylesheet" href="static/css/css.css">
    <link rel="icon" href="static/icon/favicon.ico" />
    {{ turbo() }}
</head>

<body>
    <div class="container-fluid"><img id="Camera" src="{{ url_for('video') }}"{{video}} >
        
        <div id="load" class="row" >
            <div class="col-sm-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center"><img class="Icons" src="static/img/Icon_Angle.png">
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">X : {{angleX}}</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center"><img class="Icons" src="static/img/Icon_Angle.png" >
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">Y : {{angleY}}</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center"><img class="Icons" src="static/img/Icon_Angle.png">
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">Z : {{angleZ}}</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center"><img class="Icons" src="static/img/Icon_Battery.png" style="transform: rotate(270deg);">
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">{{batterie}}%</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center"><img class="Icons" src="static/img/Icon_Battery.png" style="transform: rotate(270deg);">
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere" >S {{batterieServo}}%</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center"><img class="Icons" src="static/img/Icon_Obstacle.png">
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">{{obstacleDist}} mm</p>
                    </div>
                </div>
            </div>
        </div>
        <div id="Row_Center"class="row">
            <div class="col-sm-4"></div>
            <div class="col-sm-4"></div>
            <div id="plotdiv" class="col-sm-4 d-sm-flex d-xl-flex justify-content-sm-end justify-content-xl-end align-items-xl-center">
                <img id="plot" class="border rounded-circle border-dark" alt="plot" src="{{ url_for('plot') }}"{{plot}}>
            </div>
        </div>
        <form method="post" action="#">
            <div class="row">
                <div class="col-sm-3 col-xl-2" id="div_Buttons">
                    <div class="row">
                        <div class="col d-sm-flex justify-content-sm-center align-items-sm-center">
                            <button id="Avance" type="submit" name="submit_button" value="Avance" style="border: 0; padding: 0; background: none;"><img class="Buttons_Direction" src="static/img/Arrow_Up_Key_Light.png" ></button>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col d-sm-flex justify-content-sm-end align-items-sm-center">
                            <button id="Gauche" type="submit" name="submit_button" value="Gauche" style="border: 0; padding: 0; background: none;"><img class="Buttons_Direction" src="static/img/Arrow_Left_Key_Light.png" ></button>
                        </div>
                        <div class="col d-sm-flex justify-content-sm-start align-items-sm-center">
                            <button id="Droit" type="submit" name="submit_button" value="Droite" style="border: 0; padding: 0; background: none;"><img class="Buttons_Direction" src="static/img/Arrow_Right_Key_Light.png"></button>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col d-sm-flex justify-content-sm-center align-items-sm-center">
                            <button id="Arri??re" type="submit" name="submit_button" value="Recule" style="border: 0; padding: 0; background: none;"><img class="Buttons_Direction" src="static/img/Arrow_Down_Key_Light.png" ></button>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="row" style="height: 100%;">
                        <div class="col-lg-12 d-lg-flex justify-content-lg-center align-items-lg-end" style="background: url('static/img/Rectangle.svg') bottom/ contain no-repeat;">
                            <div class="row">
                                <div class="col">
                                    <button id="btn_Up_Robot" type="submit" name="submit_button" value="Init">
                                        <img id="Up_Icon" src="static/img/Up_Icon.svg">
                                    </button>
                                    <button id="btn_ShutDown" type="submit" name="submit_button" value="Shut_Down">
                                        <img id="ShutDown_Icon" src="static/img/ShutDown.svg">
                                    </button>
                                    
                                </div>
                                <div id="div_Select" class="col d-lg-flex justify-content-lg-center align-items-lg-end" >
                                    <select id="Select_Modes" name="Select_Modes" onchange='if(this.value!=0) {this.form.submit();}'>
                                        <optgroup label="Modes">
                                            <option value="0">S??lection des modes</option>
                                            <option value="controle">Mode Contr??le utilisateur</option>
                                            <option value="auto">Mode Autonome</option>
                                            <option value="suiveur">Mode Suiveur</option>
                                        </optgroup>
                                    </select>
                                </div>
                                <div class="col">
                                    <img id="Radar_Transparency" src="static/img/Transparency.png">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-sm-3 col-md-3 col-xl-3">
                    <div class="row d-sm-flex" style="margin-top: 70px;">
                        <div class="col-sm-6 d-sm-flex justify-content-sm-center">
                            <button id="Anti-Horaire" type="submit" name="submit_button" value="Rotation_AntiHoraire" style="border: 0; padding: 0; background: none;"><img class="Buttons_Rotation" src="static/img/Vive_Touch_Scroll_Left.png"></button>
                        </div>
                        <div class="col-sm-6 d-sm-flex justify-content-sm-center">
                            <button id="Horaire" type="submit" name="submit_button" value="Rotation_Horaire" style="border: 0; padding: 0; background: none;"><img class="Buttons_Rotation" src="static/img/Vive_Touch_Scroll_Right.png"></button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
        <div id="info" class="row" >
            <div class="col-sm-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center">
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">ip: 10.5.51.36</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-2 col-lg-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center">
                        <div id="Pulse_Connection" ></div>
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">Connection</p>
                    </div>
                </div>
            </div>
            <div class="col-sm-2 col-lg-2">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center">
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">Ping: </p>
                    </div>
                </div>
            </div>
            <div class="col-sm-2 col-lg-3">
                <div class="row">
                    <div class="col d-sm-flex align-items-sm-center">
                        <p class="d-sm-flex justify-content-sm-center align-items-sm-end Valeurs_Banniere">Packets:</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="../static/bootstrap/js/bootstrap.min.js"></script>
    <script src="../static/javascript/js.js"></script>
</body>

</html>
````