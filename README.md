Application Flask d'inscription et de connexion sécurisées
Cette application est conçue pour gérer l'inscription et la connexion des utilisateurs à un système. Elle utilise Flask, un framework web minimaliste en Python.

Installation:
Clonez ce dépôt sur votre machine locale.
Assurez-vous d'avoir Python installé sur votre système.
Installez les dépendances en exécutant pip install -r requirements.txt.
Exécutez l'application en lançant python app.py.




Structure du Projet:
app.py: Ce fichier contient le code principal de l'application, y compris la configuration de Flask et la gestion des routes.
utilisateurs.db: Fichier de base de données SQLite contenant les informations sur les utilisateurs et les connexions.
static/: Ce répertoire contient les fichiers statiques tels que les feuilles de style CSS, les images et les scripts JavaScript.
templates/: Ce répertoire contient les modèles HTML utilisés par l'application Index.html et inscription.html



Fonctionnalités Principales:
Inscription Utilisateur: Les utilisateurs peuvent s'inscrire en fournissant un identifiant et un mot de passe. Le mot de passe est crypté avant d'être stocké dans la base de données.

Connexion Utilisateur: Les utilisateurs peuvent se connecter en fournissant leur identifiant et leur mot de passe. Les informations sont vérifiées par rapport à celles stockées dans la base de données.
Gestion des Erreurs: Des messages d'erreur appropriés sont affichés en cas d'identifiant déjà utilisé, de mot de passe incorrect, etc.
Enregistrement des Connexions: Chaque connexion réussie est enregistrée dans la base de données avec l'identifiant de l'utilisateur et la date/heure de connexion.
Protection CSRF : La protection CSRF est utilisée pour sécuriser les formulaires contre les attaques CSRF.



Utilisation:
Accédez à l'application dans votre navigateur à l'adresse http://localhost:5000.
Vous serez redirigé vers la page de connexion où vous pouvez vous connecter avec vos identifiants ou créer un nouveau compte.
Après une connexion réussie, vous serez accueilli avec un message de bienvenue.




Technologies utilisées:
- Python
- Flask
- SQLite
- HTML/CSS
-javascript


