# Conclusion

## À finir dans le projet

Malheureusement dans ce projet, je n’ai pas pu finir tout ce qui était dans mon <a href="../CDC">cahier des charges</a>. Voici la liste de ce que je n’ai pas pu achever et le problème qui me bloque:

### Idées non réalisées
- Les mouvements du robot:

Je n’ai pas pu finir les mouvements du robot, parce que ça prend beaucoup de temps a les faires, puis j’avais un problème sur toute la moitié du projet qui faisait freeze le raspberry pi. Il se bloquait, car j’utilisais la connexion SSH de Visual Studio Code, qui consomme beaucoup trop et qui faisait surchauffer le raspberry pi. Pour résoudre ce souci, j’ai arrêté d’utiliser Visual Studio Code et je me suis servi de puTTY qui son utilisation est quasi nulle.

- L’algorithme Suiveur:

Avec le temps qui me restait dans les derniers jours, avec la documentation à faire, je n’ai pas pu implémenter cette fonctionnalité. J’ai pu faire la détection de QRCode, mais il me manquait le fait de décider s’il faut se tourner à gauche ou à droite dépendamment d’où est détecté le QRCode sur l’image. Puis, avancer ou reculer grâce à la détection par le lidar.

- Mettre le robot sur batterie:

Je n’ai pas mis le robot sur batterie, car il consomme beaucoup trop quand les servomoteurs sont actifs. Il consomme entre 3 [A] et 5 [A], une batterie normale se déchargerait extrêmement vite. Et il y a le problème du serpent qui se mord la queue. Si je mets une batterie assez grande pour fournir les 5 [A], il me faut des servomoteurs plus puissants, car ça sera une batterie lourde. Et si je mets des servomoteurs plus puissants, ils consommeront plus donc il faut une plus grosse batterie.

- Monter/Descendre des escaliers:

Cette idée n’a pas été réalisée, car les mouvements ne sont pas finis, et il aurait fallu avoir le feedback des servomoteurs puis des boutons sur chaque patte pour savoir la hauteur de la marche d’escalier.

### Fonctionnalités avec des bugs

La ligne de carré:

Dans le retour caméra, il y a une ligne de carré que sert à voir par rapport à la vue de la caméra et la distance que détecte le lidar, la distance entre le robot et les obstacles en face de lui. Cette fonctionnalité marche dans son ensemble, sauf qu’il a un bug où les valeurs ne se remettent pas à 0 directement.

Changement de mode:

Au changement de mode, je ne sais pas pourquoi, il y a toujours un bug avec la caméra qui surgit. Le bug est que pour créer les carrés j’ai besoin d’une image, et qu’au changement je n’ai plus de retour vidéo, et ça me renvoie une alerte. Mais si on recharge la page web, tout revient à la normale et nous sommes dans le bon mode.

## Améliorations possibles

### Servomoteurs plus puissants

L’un des gros problèmes de ce projet fut que j’ai mal dimensionné les servomoteurs, ils ne sont pas assez forts pour que le robot fasse des mouvements à l’aise.

### Optimisation

Je pense que le code n’est pas très propre par moment, par conséquent que l’on pourrait optimiser certaine partie du code qu’il s’agisse de performance ou tout simplement de suppression de redondance dans certain cas. De plus, je pense que l’utilisation du lidar branché sur les pins du GPIO du Raspberry Pi 3 serait moins coûteuse énergétiquement et la transmission des données plus rapide.

### Ajout de modes

Grâce à tous les capteurs intégrés au robot, on pourrait ajouter plein de modes différents tels que:

- L’inverse du suiveur donc le fuyard

De la façon dont j’imagine se mode est que dès qu’il détecte le QR Code, le robot hexapode fuirait dans n’importe quel sens sauf celui où il a détecté le QR Code.

- Création de chemin

Ce mode serait le fait que grâce à la caméra, l’utilisateur place des points et que le robot suive ce parcours.

Et un moyen pour que n’importe quel utilisateur puisse créer leurs propres modes.

## Bilan personnel

Durant ce travail de diplôme, il s’est passé un nombre incalculable d’évènements, des bons comme des mauvais. Ces deux derniers mois ont mis mes connaissances informatiques à rude épreuve. Malgré les divers problèmes que j’ai pu rencontrer durant l’élaboration du ce projet, je suis très fier de ce que j’ai réussi à produire avec les connaissances actuelles. Surtout en n’étant pas un professionnel dans le domaine de l’informatique. Durant ces deux mois, j’ai pu apprendre beaucoup de choses.

La première est qu’il est nécessaire d’avoir une approche méthodique et organisée face au travail qui nous est demandé de réaliser. Pour ma part, je devais réaliser une application capable de contrôler un robot hexapode à distance, tout en devant interagir avec les composants suivant:

- Caméra
- RPLidar
- Gyroscope
- Servomoteurs

Et de récupérer les données de certains de ces composants. Les éléments principaux que je n’ai pas pu implémenter, ça a été les mouvements en général du robot. J’arrive à le faire se lever, et il avance, mais je n’ai pas fait toutes les autres animations, car ça demande beaucoup de temps. Cependant, on peut avoir accès au radar 360° en temps réel. De plus, avec mon projet on peut contrôler un hexapode à distance et interagir en temps réel avec les capteurs attachés à lui à l’aide de son téléphone portable.

La seconde est qu’avoir une approche méthodique et rigoureuse est très important, car c’est en décomposant les diverses thématiques que l’on peut plus aisément prévoir les points bloquants afin de les résoudre. En plus de toutes les connaissances que j’avais, décomposer les problèmes auxquels j’ai fait face, m’aurais permis de les résoudre plus aisément.

La troisième est la vitesse de réflexion qu’il faut avoir. Pour un projet aussi conséquent que celui-là, il n’aurait pas fallu réfléchir des journées entières pour savoir où était le problème, savoir comment faire une certaine fonctionnalité, etc. J’aurais dû savoir bien à l’avance tout ce que j’avais à faire et avoir déjà une idée de comment le faire.

C’est pourquoi je suis fier de ce que j’ai réalisé durant ce travail de diplôme et que s’il m’était demandé de refaire un projet similaire, je sauterais sur l’occasion sans hésiter. Pouvoir créer quelque chose dans la robotique est très satisfaisant.