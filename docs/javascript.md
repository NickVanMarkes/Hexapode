# Script Javascript
````javascript
let toggleRadar=false 
let toggleBackGroundRadar=false 

/**
 * @function toggleSizeRadar
 * @description Toggle la taille du radar.
 * @param {void}
 * @returns {void}
 * @author Nicolas Oliveira
 */
document.getElementById('plot').addEventListener('click', () => {
    toggleRadar=!toggleRadar
    if(toggleRadar){
        document.getElementById('plot').style.transform = "translate(-75%, 50%) scale(2)";
    }
    else{
        document.getElementById('plot').style.transform = "scale(1) translate(0, 0)";
    }
});
/**
 * @function toggleBGRadar
 * @description Toggle l'arrière plan du radar.
 * @param {void}
 * @returns {void}
 * @author Nicolas Oliveira
 */
document.getElementById('Radar_Transparency').addEventListener('click', () => {
    toggleBackGroundRadar=!toggleBackGroundRadar
    if(toggleBackGroundRadar){
        document.getElementById('plot').style.backgroundColor = 'WHITE' ;
    }
    else{
        document.getElementById('plot').style.backgroundColor = 'TRANSPARENT' ;
    }
});

/**
 * @function binding
 * @description Bind les évènements sur les boutons.
 * @param {void}
 * @returns {void}
 * @author Nicolas Oliveira
 */
//si j'appuye sur T sur le clavier, le bouton "Radar_Transparency" s'active
document.addEventListener('keydown', (event) => {
    if (event.key == 't') {
        document.getElementById('Radar_Transparency').click();
    }
});

//si j'appuye sur W sur le clavier, le bouton "Avance" s'active
document.addEventListener('keydown', (event) => {
    if (event.key == 'w') {
        document.getElementById('Avance').click();
    }
});

//si j'appuye sur A sur le clavier, le bouton "Gauche" s'active
document.addEventListener('keydown', (event) => {
    if (event.key == 'a') {
        document.getElementById('Gauche').click();
    }
});

//si j'appuye sur S sur le clavier, le bouton "Arrière" s'active
document.addEventListener('keydown', (event) => {
    if (event.key == 's') {
        document.getElementById('Arrière').click();
    }
});

//si j'appuye sur D sur le clavier, le bouton "Droit" s'active
document.addEventListener('keydown', (event) => {
    if (event.key == 'd') {
        document.getElementById('Droit').click();
    }
});

//si j'appuye sur flèche gauche sur le clavier, le bouton "Anti-Horaire" s'active
document.addEventListener('keydown', (event) => {
    if (event.key == 'ArrowLeft') {
        document.getElementById('Anti-Horaire').click();
    }
});

//si j'appuye sur flèche droit sur le clavier, le bouton "Horaire" s'active
document.addEventListener('keydown', (event) => {
    if (event.key == 'ArrowRight') {
        document.getElementById('Horaire').click();
    }
});

//si j'appuye sur I sur le clavier, le bouton "Init" s'active
document.addEventListener('keydown', (event)=>{
    if (event.key == 'i'){
        document.getElementById('btn_Up_Robot').click()
    }
});

//si j'appuye sur X sur le clavier, le bouton "ShutDown" s'active
document.addEventListener('keydown', (event)=>{
    if (event.key == 'x'){
        document.getElementById('btn_ShutDown').click()
    }
});
````