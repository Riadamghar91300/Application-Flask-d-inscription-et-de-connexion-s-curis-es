from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

import sqlite3
import hashlib
import os

app = Flask(__name__)

# Génération d'une clé secrète aléatoire
clé_secrète = os.urandom(24)
clé_secrète_hex = clé_secrète.hex()

# Définition de la clé secrète pour l'application Flask
app.config['SECRET_KEY'] = clé_secrète_hex

csrf = CSRFProtect(app)

# Fonction pour initialiser la base de données
def init_db():
    # Connexion à la base de données
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()

    # Création de la table pour les utilisateurs si elle n'existe pas
    c.execute('''CREATE TABLE IF NOT EXISTS utilisateurs
                 (id INTEGER PRIMARY KEY, identifiant TEXT, mot_de_passe TEXT)''')
    
    # Création de la table pour les connexions
    c.execute('''CREATE TABLE IF NOT EXISTS connexions
                 (id INTEGER PRIMARY KEY, identifiant TEXT, date_connexion TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Appeler la fonction pour initialiser la base de données
init_db()

# Fonction pour inscrire un nouvel utilisateur dans la base de données avec mot de passe crypté
def inscrire_utilisateur(identifiant, mot_de_passe):
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()
    
    # Vérifier si l'identifiant est déjà utilisé
    c.execute('''SELECT * FROM utilisateurs WHERE identifiant=?''', (identifiant,))
    existing_user = c.fetchone()
    if existing_user:
        conn.close()
        return "Cet identifiant est déjà utilisé. Veuillez en choisir un autre."
    
     # Hasher le mot de passe
    mot_de_passe_hash = hashlib.sha256(mot_de_passe.encode()).hexdigest()

    # Vérifier si le mot de passe est déjà utilisé (hashé)
    c.execute('''SELECT * FROM utilisateurs WHERE mot_de_passe=?''', (mot_de_passe_hash,))
    existing_password = c.fetchone()
    if existing_password:
        conn.close()
        return "Ce mot de passe est déjà utilisé. Veuillez en choisir un autre."
    
    # Insérer l'utilisateur avec le mot de passe hashé dans la base de données
    c.execute('''INSERT INTO utilisateurs (identifiant, mot_de_passe) VALUES (?, ?)''', (identifiant, mot_de_passe_hash))
    conn.commit()
    conn.close()
    return "Utilisateur inscrit avec succès"


# Fonction pour vérifier les informations d'identification
def check_credentials(identifiant, mot_de_passe):
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()
    
    # Récupérer le mot de passe hashé pour l'identifiant donné
    c.execute('''SELECT mot_de_passe FROM utilisateurs WHERE identifiant=?''', (identifiant,))
    result = c.fetchone()
    
    if result:
        mot_de_passe_hash = result[0]
        # Hasher le mot de passe fourni pour le comparer avec le mot de passe hashé stocké
        mot_de_passe_hash_fourni = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        if mot_de_passe_hash == mot_de_passe_hash_fourni:
            conn.close()
            return True
    conn.close()
    return False

# Fonction pour enregistrer les informations de connexion dans la base de données
def enregistrer_connexion(identifiant):
    conn = sqlite3.connect('utilisateurs.db')
    c = conn.cursor()
    c.execute('''INSERT INTO connexions (identifiant) VALUES (?)''', (identifiant,))
    conn.commit()
    conn.close()
    print("Connexion enregistrée avec succès")

# Définition des formulaires avec Flask-WTF
class LoginForm(FlaskForm):
    identifiant = StringField('Identifiant', validators=[InputRequired()])
    mot_de_passe = PasswordField('Mot de passe', validators=[InputRequired()])
    submit = SubmitField('Valider')

class InscriptionForm(FlaskForm):
    identifiant = StringField('Identifiant', validators=[InputRequired()])
    mot_de_passe = PasswordField('Mot de passe', validators=[InputRequired()])
    submit = SubmitField("S'inscrire")

# Route par défaut pour la racine de l'application
@app.route('/')
def index():
    return redirect(url_for('connexion'))

# Route pour le formulaire d'inscription
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = InscriptionForm()
    if form.validate_on_submit():
        identifiant = form.identifiant.data
        mot_de_passe = form.mot_de_passe.data
        message = inscrire_utilisateur(identifiant, mot_de_passe)
        return message
    return render_template('inscription.html', form=form)

# Route pour le formulaire de connexion
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    form = LoginForm()
    if form.validate_on_submit():
        identifiant = form.identifiant.data
        mot_de_passe = form.mot_de_passe.data
        
        # Vérifier les informations d'identification
        if check_credentials(identifiant, mot_de_passe):
            # Enregistrer la connexion
            enregistrer_connexion(identifiant)
            return "Connexion réussie. Bienvenue !"
        else:
            return "Identifiant ou mot de passe incorrect"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
