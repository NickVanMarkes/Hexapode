# Journal de bord
## Avril
### 04.04.2022

Aujourd'hui, nous avons eu une petite introduction faite par M. Bonvin et M. Garcia sur le déroulement général du travail de diplôme. Ensuite, j'ai commencé à préparer mon environnement de travail, faire un planning prévisionnel ( chose dont je ne suis pas très bon, car je n'arrive pas souvent à préparer ce que j'ai à faire en avance ), un Trello avec mes tâches puis finalement faire le git afin que mon professeur qui me suis durant le travail de diplôme ( M. Bonvin ), puisse suivre mon avancée. Durant cette première journée on peut donc dire que j'ai juste tout bien préparer afin de commencer sérieusement le TD. À la fin de la journée nous avons eu une visite à l'HEPIA.

### 05.04.2022

Ce matin, j'ai commencé par essayer de règler le soucis que j'avais déjà sur l'interface web, qui était que je prennais trop de temps pour afficher la vue radar. ce qui m'as pris toute la matinée en essayant moultes méthodes différentes, et finalement je n'ai pas réussis à finir l'optimisation, car M. Bonvin est venu me parler de la mécanique du robot. Puis, j'ai donc commencé à visser les parties que je pouvais du robot. Enfin, à la fin de la journée, M. Bonvin est venu pour me parler d'une technique afin de savoir où se situent les pattes, grâce à l'accelèromètre et grâce au gyroscope. la technique consiste à mettre le robot sur une surface platte, lever les pattes, et de prendre ce point comme le point 0, et ainsi tester les moteurs les uns après les autres, et ainsi on peut savoir quand est-ce qu'il touchent le sol et déterminer leurs position à tout moment. Durant son explication, M. Bonvin à remarquer que les hanches du robot, n'étaient pas solidement attachées au reste du robot. On a commencé à penser pour résoudre ce soucis, et l'idée la plus prometteuse est de prendre un servomoteur en metal afin qu'il y ai le moins de jeu possible.

### 06.04.2022

Aujourd'hui, J'ai passé ma journée à essayer de résoudre le problème avec l'interface Web. Malheureusement, je ne comprends pas pourquoi le plot, pour faire la vue radar, ne veux pas fonctionner. J'ai regardé dans l'inspecteur du navigateur et je voyais que les images prennaient beaucoup trop de temps à être téléchargés (environ 2 à 5 secondes) et je ne sais pas s'il faut compresser les images pour que ça s'envois plus vite, car au niveau du raspberry pi il n'est pas surchargé.

### 07.04.2022

Ce matin, je continue à essayer de résoudre le problème de la vue radar, sauf que rien ne marche, les images prennet encore trop de temps à arriver au navigateur. J'ai donc décider de laisser ça de coté et attendre que M.Bonvin puisse m'aider sur ce problème, et j'ai commencé à afficher l'information de la distance de l'obstacle le plus proche sur la bannière sur le haut de l'interface.
A midi, M. Bonvin est passé dans la classe et m'as ramené des caisses remplies de composants de chez lui, ainsi que les connecteurs afin de faire les rallonges pour les servos. Ensuite, il m'as expliqué en très rapide ce qu'il fallait faire pour résoudre mon soucis: 
- Faire une classe externe qui gère la création des plots
- On s'en fout du web et on fait en sorte que ça créer les plots hors web
- Dès que tout fonctionne, intégrer cette classe dans le web
- Faire une documentation de cette classe et expliquer tout ce que je fait au mieux

En regardant mon trello, je trouve que je passe beaucoup trop de temps sur ce problème avec les plots. Il faut donc que je le règle au plus vite. Je pense refaire comme pour le travail de semestre et travailler le soir chez moi pour faire en sorte que ça marche.
Après les cours j'ai fait le programme que m'avais dit M. Bonvin, et j'ai remarqué que le message "Start" du lidar prennais trop de temps à venir, et j'ai vérifié en mettant plein de timers et matplotlib prends 5.51 secondes à être importer alors que les autre 5 mS. Il faudrait donc que je m'informe envers M. Bonvin sur ce qu'il prends autant de temps et pourquoi.

### 08.04.2022

Ce matin, j'ai continué à travailler sur le débugage de de la vue radar, et M. Bonvin m'as appelé en me disant de faire un autre script, et m'as dit de prendre le code d'exemple. Puis, ne voyant toujours pas le bout de la solution à se problème, j'ai commencé à faire le câblage pour les rallonges des servos moteurs, car aujourd'hui j'ai reçu la commande avec les gaines thermoretractables. Ensuite je les ai essayée, en regardant dans les pires position voir si tout était assez long, et tout est comme il faut. Puis, vers la fin de la journée, je me suis réattaqué sur la solution de la vue radar. En testant, j'ai vu que même avec l'exemple cela prennait 30 secondes pour avec 400 scans. Mais en regardant ce qu'il y avait dans les 400 scans, il y avait 400*360°, ce qui est problématique. J'ai essayé alors avec 1 seul scan, il y manque beaucoup d'information, car il prend que de là où il est en ° jusqu'à ~360°. De ce fait, pour être sûr d'avoir toutes les infos, 2 scans sont nécessaires, ce qui prend 0.46 secondes.