# CSS
````css
body{
    width: 100vw!important;
    height: 100vh!important;
    overflow: hidden!important;
}

#Camera{
    height: 100%; 
    width: 100%; 
    position: absolute; 
    bottom: -1px; 
    left: -1px; 
    right: -1px;
    top: -1px; 
    z-index: -50;
}

#load{
    background: rgba(0,0,0,0.6);
    width: 100%;
    left: 10px;
    right: 0;
}

.Icons{
    width: 17px;
    height: 17px;
}

.Valeurs_Banniere{
    width: 100%;
    height: 30px;
    font-size: 16px;
    margin-bottom: 0px;
    color: var(--bs-white);
    font-family: Roboto, sans-serif;
}

#info{
    position: absolute;
    bottom: 0;
    right: 0;
    left: 10px;
    background: rgba(0,0,0,0.6);
}

#Row_Center{
    height: 150px;
}

#plot{
    width: 250px;
    height: 250px;
    background-color: rgb(0, 0, 0, 0.2);
}

.Buttons_Direction{
    width: 50px;
}

.Buttons_Rotation{
    width: 70px;
}

#btn_Up_Robot{
    margin-top: 130px;
    height: 100x;
    width: 100px;
    background: none;
    border: 0px;
    transform: translateY(200);

}
#Up_Icon{
    filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(75deg) brightness(100%) contrast(100%)
}
#ShutDown_Icon{
    filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(75deg) brightness(100%) contrast(100%)
}

#btn_ShutDown{
    margin-top: 0px;
    height: 100px;
    width: 100px;
    background: none;
    border: 0px;
    transform: translateX(-150px) translateY(-50px);
}

#Select_Modes{
    color: rgb(255, 255, 255);
    background: rgb(68, 68, 68);
    margin-top: 110px;
}

#div_Select{
    padding-bottom: 10%;
    
}

#Radar_Transparency{
    width: 100px;
    height: 100px;
    margin-top: 130px;
    transform:translateX(50px) ;
}
.d-lg-flex {
    display: flex!important;
}
.align-items-lg-end {
    align-items: flex-end!important;
}
.justify-content-lg-center {
    justify-content: center!important;
}
form{
    position: absolute;
    bottom: 25px;
    left: 0;
    right: 0;
}

#div_Buttons{
    padding-bottom: 20%;
}

#Pulse_Connection{
    background: rgba(0,255,0,1);
    width: 10px;
    height: 10px;
    padding-right: 10px;
    box-shadow: 10px 10px 20px green;
    border-radius: 50%;
    animation: pulsate 2s infinite;
}

@keyframes pulsate {
    0% {
        box-shadow: 0 0 4px 4px rgba(0, 255, 0, 0.2);
   }
    50% {
        box-shadow: 0 0 5px 5px rgba(0, 255, 0, 0.1);
    }

    100% {
        box-shadow: 0 0 4px 4px rgba(0, 255, 0, 0.2);
    }
}

/* CSS for Extra Large (xl) screen */
@media only screen and (max-width: 1440px) {
    #plot{
        width: 250px;
        height: 250px;
    }
    #Radar_Transparency{
        width: 75px;
        height: 75px;
        margin-top: 110px;
        transform:translateX(50px);
    }

    #btn_Up_Robot{
        margin-top: 110px;
        height: 75x;
        width: 75px;
        background: none;
        border: 0px;
        transform: translateX(50px);
    }

    #btn_ShutDown{
        height: 75px;
        width: 75px;
        background: none;
        border: 0px;
        transform: translateX(0px) translateY(-75px);
    }
    
}

/* CSS for Extra Large (xl) screen */
@media only screen and (max-height: 550px) {
    
    #div_Buttons{
        padding-bottom: 0;
    }
}

/* CSS for Extra Large (xl) screen */
@media only screen and (max-width: 1366px) {
    #plot{
        width: 200px;
        height: 200px;
    }
    #Radar_Transparency{
        width: 75px;
        height: 75px;
        margin-top: 150px;
        transform:translateX(50px) translateY(40px);
    }

    #btn_Up_Robot{
        margin-top: 150px;
        height: 75x;
        width: 75px;
        background: none;
        border: 0px;
        transform: translateX(50px) translateY(40px);
    }
    #btn_ShutDown{
        height: 75px;
        width: 75px;
        background: none;
        border: 0px;
        transform: translateX(-30px) translateY(-25px);
    }
    
}

/* CSS for Large (lg) screen */
@media only screen and (max-width: 1280px) {
    #plot{
        width: 180px;
        height: 180px;
    }
}

/* CSS for Large (lg) screen */
@media only screen and (max-width: 1280px) {
    #plot{
        width: 180px;
        height: 180px;
    }
}

/* CSS for Large (lg) screen */
@media only screen and (max-width: 1152px) {
    #plot{
        width: 170px;
        height: 170px;
    }
    #Radar_Transparency{
        width: 50px;
        height: 50px;
        margin-top: 110px;
        transform:translateX(50px) translateY(40px);
    }

    #btn_Up_Robot{
        margin-top: 120px;
        height: 50px;
        width: 50px;
        background: none;
        border: 0px;
        transform: translateX(50px) translateY(30px);
    }
    #btn_ShutDown{
        height: 50px;
        width: 50px;
        background: none;
        border: 0px;
        transform: translateX(0px) translateY(-20px);
    }
    
}

/* CSS for Large (lg) screen */
@media only screen and (max-width: 1024px) {
    #plot{
        width: 160px;
        height: 160px;
    }
    
}

/* CSS for Large (lg) screen */
@media only screen and (max-width: 992px) {
    #plot{
        width: 150px;
        height: 150px;
    }
}

/* CSS for Medium (md) screen */
@media only screen and (max-width: 800px) {
    #plot{
        width: 140px;
        height: 140px;
    }
    #Radar_Transparency{
        width: 50px;
        height: 50px;
        margin-top: 110px;
        transform:translateX(25px);
    }

    #btn_Up_Robot{
        margin-top: 110px;
        height: 50x;
        width: 50px;
        background: none;
        border: 0px;
        transform: translateX(25px);
    }
    #btn_ShutDown{
        margin-top: 0px;
        height: 50px;
        width: 50px;
        background: none;
        border: 0px;
        transform: translateX(0px) translateY(-25px);
    }
    
}

/* CSS for Medium (md) screen */
@media only screen and (max-width: 768px) {
    #plot{
        width: 130px;
        height: 130px;
    }
    #Radar_Transparency{
        width: 25px;
        height: 25px;
        margin-top: 120px;
        transform:translateX(0px);
    }

    #btn_Up_Robot{
        margin-top: 110px;
        height: 25x;
        width: 25px;
        background: none;
        border: 0px;
        transform: translateX(0px);
    }
    #btn_ShutDown{
        margin-top: 0px;
        height: 25px;
        width: 25px;
        background: none;
        border: 0px;
        transform: translateX(0px) translateY(-25px);
    }
    
}

/* CSS for Medium (md) screen */
@media only screen and (max-width: 600px) {
    #plot{
        width: 120px;
        height: 120px;
    }
    #Radar_Transparency{
        width: 25px;
        height: 25px;
        margin-top: 120px;
        transform:translateX(0px);
    }
    #div_Select{
        padding-bottom: 0%;
        transform: translateY(130px);
        
    }

    #btn_Up_Robot{
        margin-top: 120px;
        height: 25x;
        width: 25px;
        background: none;
        border: 0px;
        transform: translateX(0px);
    }
    #btn_ShutDown{
        margin-top: 110px;
        height: 25px;
        width: 25px;
        background: none;
        border: 0px;
        transform: translateX(0px);
    }
    

}

/* CSS for Extra Small (xs) screen */
@media only screen and (max-width: 414px) {
    #plot{
        width: 110px;
        height: 110px;
    }
    
}

/* CSS for Extra Small (xs) screen */
@media only screen and (max-width: 394px) {
    #plot{
        width: 100px;
        height: 100px;
    }
    
    
}

/* CSS for Extra Small (xs) screen */
@media only screen and (max-width: 375px) {
    #plot{
        width: 90px;
        height: 90px;
    }
    
}

/* CSS for Extra Small (xs) screen */
@media only screen and (max-width: 360px) {
    #plot{
        width: 80px;
        height: 80px;
    }
    
    
}

/* CSS for Extra Small (xs) screen */
@media only screen and (max-width: 320px) {
    #plot{
        width: 70px;
        height: 70px;
    }
    
    
}
````