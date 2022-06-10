# Cahier des charges

## Sujet
Création d’un robot capable de se déplacer de manière autonome, ainsi que d’être contrôlé par quelqu’un.

## But du projet
Ce projet a pour but de fabriquer un robot hexapode, qui aura comme fonctionnalités:

* Pouvoir se déplacer sur le sol (pente ou pas).
* Monter/Descendre des escaliers.
* Détecter toute sorte d’obstacles autour de lui.
* Pouvoir être autonome.
* Pouvoir être contrôlé par un téléphone grâce à une application.
* (optionnel) Pouvoir être contrôlé par une télécommande.
## Spécification

Ce robot sera fait de A à Z par mes soins, modéliser les pièces en 3D, les imprimer grâce à une imprimante 3D, monter le tout, et aussi programmer le robot ainsi que l’application pour le smartphone.<br/>

Ce robot comporte trois modes principaux: un mode autonome ainsi qu’un mode contrôlé par un utilisateur.<br/>
Dans le mode autonome, le robot pourra marcher, éviter les obstacles grâce au lidar, puis monter des marches tout seul, et si le robot par malchance se retourne, il y aura un gyroscope pour qu’il puisse détecter le fait qu’il soit à l’envers, et ainsi, il puisse se retourner.<br/>
Ensuite, il y a le mode utilisateur, qui lui, permettra à une personne de contrôler le robot grâce à un smartphone,
et qui pourra faire plusieurs fonctionnalités, par exemple: faire un saut, désactiver les capteurs, contrôler la vitesse de marche, activer la caméra, etc.
Et finalement, le mode suiveur, où le robot détectera une personne devant lui grâce à la caméra et ainsi la suivra partout où elle ira.

L’avantage de faire un robot hexapode, est que nous pouvons décider de la hauteur du robot, par exemple, nous pouvons décider qu’il soit à ras du sol, comme nous pourrons décider qu’il soit sur la pointe des pattes. Ensuite, autre avantage, est que vu qu’il a 6 pattes, il pourra être stable sur 4 pattes et ainsi avoir 2 pattes, pour faire certaines actions, comme pousser une porte, déplacer un objet, ou voire même pouvoir le tenir entre 2 pattes. Et enfin, le dernier avantage, c’est que vu que c’est des pattes et pas des roues, le robot pourra descendre et monter des escaliers ainsi que grimper certains obstacles.

Ensuite, afin d’avoir une certaine stabilité électriquement parlant, j’ai décidé de mettre 2 batteries sur le robot. Une sera pour alimenter le raspberry pi ainsi que tous les modules, et l’autre sera là pour alimenter que les servos, car c’est ce qui va tirer le plus de courant, ce système est fait pour qu’il n’y ai aucun problème avec un manque de courant pour le raspberry pi.


### Spécification des différents modules
* Lidar: composant qui fait une cartographie de l’environnement afin de détecter les obstacles autour du robot.
* Sonar: composant qui envoie un ultrason au sol avec un certain angle afin de détecter s’il y a un vide en face du robot.
* PCA9685: composant qui sert à gérer plusieurs servomoteurs en même temps.
* MPU6050: gyroscope et accéléromètre qui servira à détecter si le robot, c’est retourné, ainsi que son accélération.
* Camera: caméra qui sera utile pour que l’utilisateur puisse voir sur son smartphone une vue par rapport au robot.

### To do list
* Déterminer la consommation générale du robot afin de calculer une batterie adéquate pour minimum 2 h d’autonomie.
* En fonction des servomoteurs, déterminer la vitesse maximale à laquelle le robot pourra se déplacer.
* En fonction des servomoteurs, déterminer la charge totale que pourrait recevoir le robot.
* Réalisation des pièces en 3D, car s’il y a des problèmes avec l’imprimante 3D, toutes les pièces prendront beaucoup trop de temps à être fabriquées.
* Réalisation d’une carte pouvant charger les deux batteries du robot.


## Restrictions

* Début le 4 Avril au 10 Juin
* Les pièces 3D doivent déjà être utilisables
* utilisation majeure du python (cause raspberry pi)
* Utilisation d’un oscilloscope
* (Utilisation du Lidar)


## Parties prenantes

| Nom|Fonction |
|:-:|:-:|
| Pascal Bonvin | Professeur |
| Nicolas Oliveira | Élève |

## Analyse de l’existant

- lynxmotion <a href="http://www.lynxmotion.com/c-117-phoenix.aspx">Phoenix </a>

Cet hexapode de chez lynxmotion est un robot intéressant et imposant. Malheureusement, il n’a aucun capteur, il lui est donc impossible d’être autonome, il lui faut donc être contrôlé par l’utilisateur.

- Adeept <a href="https://www.adeept.com/learn/detail-37.html">RaspClaws</a>

Cet hexapode de chez Adeept est un robot ressemblant à celui de chez lynxmotion. La valeur ajoutée est qu’il y a une caméra d’installée dessus. Mais aucun autre capteur n’est installé dessus. Donc, comme celui au dessus il lui est impossible d’être autonome.

- EZ-Robot <a href="https://www.ez-robot.com/store/p9/spider-robot/hexapod-robot-kit.html"> Hexapod</a>

Cet hexapode de chez EZ-Robot, est le plus intéressant que j’ai pu trouver. Il a une interface pour mobile qui permet d’être contrôlé à distance, avec intégré le retour caméra. Mais comme pour les autres, c’est le seul capteur implémenté dessus.

Comme on peut le voir, est que mon robot à des capteurs qui lui permettent d’être autonome. Par exemple, le lidar qui permet à mon hexapode de détecter des obstacles même derrière lui. Ensuite, le gyroscope afin de pouvoir le stabiliser et détecter l’inclinaison du robot. Puis, comme les robots au-dessus, une caméra qui me sert de retour afin d’être facilement contrôlable à distance.

## Environnement
### Langage de programmation
* Python
* peut-être web (python Flask)
### Système d’exploitation
* Raspbian
### Matériel
* Ordinateur personnel
* Imprimante 3D
* Raspberry Pi
### Software
* SolidWorks (CAO)
* Visual Studio Code
* KiCad (carte recharge des batteries)

## Livrables
* Documentation
* Journal de bord
* Code source
* Robot