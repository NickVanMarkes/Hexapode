let toggleRadar=false 
let toggleBackGroundRadar=false 

document.getElementById('plot').addEventListener('click', () => {
    toggleRadar=!toggleRadar
    if(toggleRadar){
        document.getElementById('plot').style.transform = "translate(-75%, 50%) scale(2)";
    }
    else{
        document.getElementById('plot').style.transform = "scale(1) translate(0, 0)";
    }
});

document.getElementById('Radar_Transparency').addEventListener('click', () => {
    toggleBackGroundRadar=!toggleBackGroundRadar
    if(toggleBackGroundRadar){
        document.getElementById('plot').style.backgroundColor = 'rgb(255, 255, 255, 1);' ;
    }
    else{
        document.getElementById('plot').style.backgroundColor = 'rgb(0, 0, 0, 0.2);' ;
    }
});