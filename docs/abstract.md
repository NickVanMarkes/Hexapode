# Résumé

The Big Bug est un robot hexapode (six pattes) pouvant se déplacer dans toutes les directions. Le robot est contrôlé par l'utilisateur via un smartphone, qui peut décider des actions, des animations ou le mettre dans différents modes.
Les modes fournis sont :

- Le mode contrôle utilisateur
- Le mode autonome
- Le mode suiveur
## Utilisateur
Le mode contrôle utilisateur est un mode dans lequel un utilisateur peut contrôler le robot via un site Web à l'aide d'un smartphone ou d'un ordinateur. Sur ce site, il dispose d'un retour caméra, de 4 boutons pour déplacer le robot vers l'avant/l'arrière ou vers la gauche/droite, d'une vue radar des obstacles que le lidar parvient à détecter, et d'une bannière avec les informations les plus importantes, comme l'inclinaison du robot, pourcentage de batterie et obstacle le plus proche.
## Autonome
Le mode autonome est l'endroit où nous ne contrôlons pas le robot. Il marche et une fois qu'il y a un obstacle, il décide de quel côté est le plus avantageux. Il boucle tout en faisant des animations aléatoires.
## Suiveur
Le mode suiveur est un mode où grâce à un code QR affiché à la caméra, et à la détection de la distance grâce au lidar, le robot suit la personne à tout moment, si la personne avance, le robot avancera, s'il recule, il recule, etc.
# Abstract

The Big Bug is a hexapod robot (six legs) that can move in all directions. This robot is controlled by the user with his smartphone, which can decide actions, animations or put it in different modes.
The provided modes are :

- The user-controlled mode
- Autonomous mode
- The follower mode
## User-control
The user-controlled mode is a mode where a user can control the robot with the website using a smartphone or a computer. On this website, there is a camera feedback, 4 buttons to move the robot forward/backward or left/right, a radar view of the obstacles that the lidar manages to detect, and a banner with the most important informations, such as the robot's inclination, the percentage of battery charge left and nearest obstacle.
## Autonomous
The autonomous mode is a mode where we do not control the robot, it walks, until there is an obstacle. It decides which way is better. While deciding, it walks in a circle and doing some random animations. 
## Followers
The follower mode is a mode where with a QR code, shown to the camera, it will follow a person at any time and using the LiDAR, the range needed to catch up to the person. If the person goes forward, the robot goes forward, if they goes backward, it goes backward, etc.