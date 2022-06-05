# Difficultés rencontrés

Durant la conception de ce projet, en ayant pas assez préparer et compris le fonctionnement des modules hardware. J'ai rencontré de nombreux problèmes que j'ai su résoudre, mais qui m'ont fait perdre du temps.

## Vue Radar

Pour la vue radar, visible sur l'interface en haut à droite, j'ai eu très longtemps un problème avec l'insertion des données pendant la création du plot. Ce qui faisait en sorte que la création des nouveaux plots prennaient beaucoup trop de temps. Et de ce fait, la vue était plus souvent vide qu'avec une image avec les points qui représentent les obstacles. Pour régler ce problème, j'ai examiné ce qui ne changeait jamais sur l'image (par exemple le fond, les cerles, ainsi que la distance). Puis, j'ai optimisé le code en évitant de refaire ce qui ne change pas, et de juste mettre les nouveaux points dessus.

Ensuite, j'ai remarqué que le temps de téléchargement des images prenait aussi beaucoup trop de temps. J'ai cherché longement sur internet et sur la documentation officielle de flask, le pourquoi. Malheureusement, je n'ai pas réussis à trouver un réponse concrète. J'ai essayé plusieurs techniques comme ne pas enregistrer en cache en y mettant un header, mais ça n'as pas résolu ce problème. J'ai alors pensé à faire comme avec la caméra et faire un stream de l'image (image qui est donc enregistrer et ensuite streamée). 


## Lidar

Le lidar m'a donné beaucoup de problème, ou plutôt d'incompréhension. Tout d'abord, en programmation en général, je n'ai jamais travaillé avec les exceptions et encore moins en python. En travaillant avec le lidar, j'avais beaucoup d'exceptions à prendre en compte, car si je ne les gérais pas, le programme s'arrêtait et ce n'était pas concevable que le programme s'arrête à cause d'une exception. Ce que j'ai fait pour régler ce problème, fut un try except, qui dans son nom autoexplicatif, sert à gérer les exceptions, et au lieu d'arrêter le programme, je faisais un arrêt du lidar, et le relançais.

Ensuite, en corélation avec les problèmes de la vue radar, j'ai remarqué que l'acquisition de données était un peu longue, car dans la documentation j'avais lu qu'en un tour, il enregistrait 400 données, mais dû a une mauvaise compréhension de ma part, je faisait donc une boucle for, qui enregistrait 400 tour, et pas 1 tour ( qui a l'intérieur avait 400 valeurs). Et donc, pour régler ce problème, je n'ai que changé la valeur de la boucle for à 2 tours, chiffre expliqué dans <a href="../Fonctionalite">l'analyse fonctionnelle</a>.

Puis, pour le projet, je devais faire du multithreading afin que le programme tournes tout le temps sans qu'il soit bloqué dans l'acquisiton des données du lidar constamment. La compréhension du fonctionnement du multithreading m'as pris un certain temps, mais ensuite, ce fut assez rapide et en pratiquant, j'ai remarqué que le timer de base de python, n'est pas une fonction qui lance un thread chaque x temps, mais qui lance une fois la fonction en thread mais après x temps. J'ai donc du faire ma propre classe qui reprend la fonction de base mais qui répète automatiquement la fonction en thread.

## Mouvements

Pour les mouvements du robot, ce qui a été le plus compliqué, a été de synchronisé tout les servomoteurs, car ceux que j'utilise sont des servomoteurs à rotation continue expliqué dans la partie <a href="../Composants">Composants</a> et pour résumer je n'ai pas de feedback donc ils sont à l'aveugle. Pour régler ce problème, je peux détécter les pattes grâce au lidar, et ainsi je peux un savoir l'angle où ils sont afin de faire l'initialisation, et ainsi avoir un référentiel.

Ensuite, le plus gros problème du projet, suite à une mauvaise estimation du poids total du robot, ainsi qui de la force nécéssaire par rapport à la mécanique faite, les servomoteurs n'ont pas assez de force pour soulever le robot de manière à l'aise. Et les seuls moyens pour régler ce soucis sont:

- Changer les servomoteurs

Je pourrais changer les servomoteurs et en prendre des plus puissant, sauf que cette solution est très chère, car il y a 18 servomoteurs à changer et les prix grimpent vite pour avoir de la puissance.

- Changer la mécanique

Je pourrais changer la mécanique du robot, et ainsi les moments de force seront moins important, et aussi réduire le poids des pièces en enlevant les espaces inutiles.