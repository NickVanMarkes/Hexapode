# Conclusion

## Améliorations possibles

### Servomoteurs plus puissants

L'un des gros problèmes de ce projet, fut que j'ai mal dimensionné les sevomoteurs, ils sont pas assez fort pour que le robot fasse des mouvements à l'aise.

### Optimisation

Je pense que le code n'est pas très propre par moment, par conséquent que l'on pourrait optimiser certaine partie du code qu'il s'agisse de performance ou tout simplement de suppression de redondance dans certain cas. De plus, je pense que l'utilisation du Lidar branché sur les pins du GPIO du Raspberry Pi 3 serait moins coûteux énergétiquement et la transmission des données plus rapide.

### Ajout de modes

Grâce à tout les capteurs intégrés au robot, on pourrais ajouter plein de modes différents tels que :

- L'inverse du suiveur donc le fuyard

De la façon dont j'imagine se mode est que dès qu'il détecte le QR Code, le robot hexapode fuirait dans n'importe quel sens sauf celui où il a détécté le QR Code.

- Création de chemin

Ce mode serait le fait que grâce à la caméra, l'utilisateur place des points et que le robots suive ce parcours.

Et un moyen pour que nimporte quel utilisateur puisse créer leur propre modes.

## Bilan personnel

Durant ce travail de diplôme, il s'est passé un nombre incalculable d'évènements, des bons comme des mauvais. Ces deux derniers mois ont mis mes connaissances informatique à rude épreuve. Malgré les divers problèmes que j'ai pu rencontrer durant l'élaboration du ce projet, je suis très fier de ce que j'ai réussi à produire avec les connaissances actuelles, n'étant pas un professionnel dans le domaine de l'informatique. Durant ces deux mois j'ai pu apprendre beaucoup de choses.

La première est qu'il est nécessaire d'avoir une approche méthodique et organisée face au travail qui nous est demandé de réaliser. Pour ma part, je devait réaliser une application capable de contrôler un robot hexapode à distance, tout en devant intéragir avec les composants suivant :

- Caméra
- RPLidar
- Gyroscope
- Servomoteurs

Et de récupérer les données de certains de ces composants. Les éléments principaux que je n'ai pas pu implémenter, ça a été les mouvements en général du robot. J'arrive à le faire se lever, et il avance, mais je n'ai pas fait toutes les autres animations, car ça demande beaucoup de temps. Cependant, on peut avoir accès au radar 360° en temps réel. De plus, avec mon projet on peut contrôler un hexapode à distance et interagir en temps réel avec les capteurs attachés à lui à l'aide de son téléphone portable.

La seconde est qu'avoir une approche méthodique et rigoureuse est très important, car c'est en décomposant les diverses thématiques que l'on peut plus aisément prévoir les points bloquants afin de les résoudre. En plus de toutes les connaissances que j'avais, décomposer les problèmes auxquels j'ai fait face, m'aurais permis de les résoudre plus aisément. 

C'est pourquoi je suis fier de ce que j'ai réalisé durant ce travail de diplôme et que s'il m'était demandé de refaire un projet similaire, je sauterais sur l'occasion sans hésiter, car pouvoir créer quelque chose dans la robotique est très satisfaisant.