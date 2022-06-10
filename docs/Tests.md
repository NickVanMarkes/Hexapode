# Tests

## Raspap

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 001 | Le smartphone détecte le réseau | OK | Le smartphone détecte correctement le réseau |
| 002 | Le smartphone peut se connecter au réseau | OK | - |
| 003 | Le smartphone peut accéder au site local du raspberry pi | OK | - |
| 004 | Le PC détecte le réseau | OK | Le PC détecte correctement le réseau |
| 005 | Le PC peut se connecter au réseau | OK | - |
| 006 | Le PC peut accéder au site local du raspberry pi | OK | - |

## Flask

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 011 | Serveur Flask accessible | OK | - |
| 012 | Permets l’accès à la bonne page | OK | - |
| 013 | Rafraichis correctement les données | OK | Le rafraîchissement se fait correctement et toutes les secondes |

## Mobile

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 021 | La taille est adaptée au smartphone | OK | - |
| 022 | Les boutons apparaissent aux bons endroits | OK | - |
| 023 | Les boutons contiennent les bonnes informations | OK | - |
| 024 | La caméra est active? | OK | La caméra affiche correctement sur le support |
| 025 | La caméra est fluide? | OK | La caméra est suffisamment fluide |
| 026 | Tous les boutons de directions renvois la methode post, avec la bonne valeur | OK | - |
| 027 | Le sélecteur de modes renvois la méthode, avec la valeur du mode choisis | OK | - |
| 028 | Si l'utilisateur clique sur la vue radar, elle s'agrandit | OK | - |
| 029 | Le bouton pour choisir la transparence est fonctionnel | OK | - |

## PC

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 031 | La taille est adaptée au PC | OK | - |
| 032 | Les boutons apparaissent aux bons endroits | OK | - |
| 033 | Les boutons contiennent les bonnes informations | OK | - |
| 034 | La caméra est active? | OK | La caméra affiche correctement sur le support |
| 035 | La caméra est fluide? | OK | La caméra est suffisamment fluide |
| 036 | Tous les boutons de directions renvois la methode post, avec la bonne valeur | OK | - |
| 037 | Le sélecteur de modes renvois la méthode, avec la valeur du mode choisis | OK | - |
| 038 | Si l'utilisateur clique sur la vue radar, elle s'agrandit | OK | - |
| 039 | Le bouton pour choisir la transparence est fonctionnel | OK | - |

## Modules

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 041 | Le module Gyroscope agit correctement | OK | s'allume et intéragit avec le raspberry pi |
| 042 | Les modules PCA9685 agissent correctement | OK | s'allume et intéragit avec le raspberry pi |
| 043 | La caméra agit correctement | OK | s'allume et intéragit avec le raspberry pi |
| 044 | Les servomoteurs sont fonctionnels | OK | - |
| 045 | Le lidar agit correctement | OK | l’acquisition des données est faite rapidement |

## Classes

### Animations

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 051 | Initialise correctement tout les servomoteurs | OK | - |
| 052 | Init2 est finis et fonctionnel | OK | - |
| 053 | Avance est finis et fonctionnel | OK | - |
| 054 | Maintiens est finis et fonctionnel | OK | - |
| 055 | Recule est finis et fonctionnel | KO | Problème avec les servomoteurs expliqué <a href="../Difficulte">ici</a> |
| 056 | Droite est finis et fonctionnel | KO | Problème avec les servomoteurs expliqué <a href="../Difficulte">ici</a> |
| 057 | Gauche est finis et fonctionnel | KO | Problème avec les servomoteurs expliqué <a href="../Difficulte">ici</a> |
| 058 | Rotation_Horaire est finis et fonctionnel | KO | Problème avec les servomoteurs expliqué <a href="../Difficulte">ici</a> |
| 059 | Rotation_AntiHoraire est finis et fonctionnel | KO | Problème avec les servomoteurs expliqué <a href="../Difficulte">ici</a> |
| 060 | Off est finis et fonctionnel | OK | - |

### VideoCamera

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 151 | Initialise correctement la caméra | OK | - |
| 152 | get_frames dessine correctement les carrés sur l'image | OK | - |
| 153 | les carrés sont réactif selon les obstacles | OK | - |
| 154 | get_frames renvoit correctement l'image | OK | - |
| 155 | QRCodeDetect est finis et fonctionnel | OK | Détecte le QRCode le décripte et l'encadre sur la vidéo |

### Gyroscope

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 251 | Le gyroscope s'initialise correctement | OK | - |
| 252 | get_angle renvois correctement les données sur trois axes | OK | - |
| 253 | get_acceleration renvois correctement les données sur les trois axes | OK | - |

### Lidarasync

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 351 | Le lidar s'initialise correctement | OK | - |
| 352 | Le singleton renvois l'instance créée du lidar | OK | - |
| 353 | La propriété de la distance la plus courte est atteignable par les autres scripts | OK | - |
| 354 | Get_Data renvois correctement la liste des données récupérées par le lidar | OK | - |
| 355 | DoScan effectue correctement les scans et les exceptions sont gérées | OK | - |
| 356 | StartLidar démarre correctement le lidar | OK | - |
| 357 | StopLidar arrête correctement le lidar | OK | - |

### Motor

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 451 | La classe initialise correctement les servomoteurs | OK | - |
| 452 | SetAngleRel bouge correctement le servomoteur à un angle relatif | OK | - |
| 453 | StayWithForce garde un force minimale au servomoteur et dans la bonne direction | OK | - |
| 454 | WithoutForce enlève correctement la force du servomoteur | OK | - |

### Plot

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 551 | La classe s'initialise correctement | OK | - |
| 552 | CreatePlot récupère et interprète correctement les données du lidar | OK | - |
| 553 | Les couleurs sont en corélation avec la ligne de carrés | OK | - |
| 554 | CreatePlot renvois correctement la vue radar | OK | - |

### RepeatTimer

|ID|Description|Statut|Commentaire|
|--|--|--|--|
| 651 | La classe créé correctement un thread qui est répété en continu selon une intervalle donnée | OK | - |