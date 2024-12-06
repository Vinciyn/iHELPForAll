# iHELPForAll - Spotify Utility Tool

![Version](https://img.shields.io/badge/version-1.0-blue) ![Maintained](https://img.shields.io/badge/maintained-yes-green) ![License](https://img.shields.io/badge/license-VXO/N2L/HLP-yellow)

**iHELPForAll** est un outil d'utilitaires pour Spotify permettant de transférer, regrouper et sauvegarder des playlists, morceaux likés, albums et artistes entre différents comptes Spotify.

## 📜 Fonctionnalités

- **iTransferAll** : Transférez vos playlists, morceaux likés, albums et artistes suivis d'un compte Spotify source à un compte destination.
- **iRegroupAll** : Regroupez plusieurs playlists en une seule playlist combinée.
- **iBackupAll** : Sauvegardez vos playlists, morceaux likés, albums et artistes suivis dans un fichier JSON.

## ⚙️ Installation

### Prérequis
1. Python 3.9 ou plus.
2. [Spotipy](https://spotipy.readthedocs.io/) - Une librairie Python pour interagir avec l'API Spotify.
3. Un fichier `config.json` contenant vos **identifiants API Spotify**.

### Étapes
1. Clonez ce dépôt :
    ```bash
    git clone https://github.com/vinciyn/iHELPForAll.git
    cd spotify-utility
    ```
2. Installez les dépendances Python nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

   Si le fichier `requirements.txt` n'existe pas encore, créez-le en listant les modules suivants :
   ```bash
   pip freeze > requirements.txt
   ```
3. Configurez votre fichier `config.json` avec vos identifiants API Spotify :
    ```json
    {
      "client_id": "votre_client_id",
      "client_secret": "votre_client_secret",
      "redirect_uri": "http://localhost:8888/callback"
    }
    ```

---

## 🔑 **Obtenir les clés d'API Spotify**

Pour que l'outil fonctionne avec Spotify, vous devez obtenir vos propres clés API. Voici les étapes :

1. Connectez-vous ou inscrivez-vous sur le [Dashboard Spotify for Developers](https://developer.spotify.com/dashboard/).
2. Créez une nouvelle application et récupérez les **Client ID** et **Client Secret**.
3. Ajoutez une URL de redirection valide (par exemple : `http://localhost:8888/callback`).
4. Ajoutez ces clés à un fichier `config.json` à la racine du projet :
   ```json
    {
      "client_id": "votre_client_id",
      "client_secret": "votre_client_secret",
      "redirect_uri": "http://localhost:8888/callback"
    }
   ```

---

## 🚀 **Utilisation**

1. Lancez le programme principal :
   ```bash
   python main.py
   ```

2. Suivez les instructions affichées dans le terminal pour choisir les outils ou options que vous souhaitez utiliser.


---

## 📂 **Structure du Projet**

Voici une vue d'ensemble de la structure du projet :

```
iHELPForAll/
│
├── main.py                 # Script principal
├── requirements.txt        # Liste des dépendances Python
├── config.json             # Variables d'environnement
└── README.md               # Documentation du projet
```

---

## 🐞 **Dépannage**

### Problème : "Module not found"
Assurez-vous que les modules requis sont installés via `pip install -r requirements.txt`.

### Problème : "Clé API invalide"
Vérifiez que vos clés dans le fichier `config.json` sont correctes et que l'URL de redirection correspond à celle configurée dans le Dashboard Spotify (c'est à dire `http://localhost:8888/callback`).

---

## ✨ **Contribution**

Les contributions sont les bienvenues ! Suivez ces étapes pour participer :

1. **Fork** le projet.
2. **Clonez** votre fork en local :
   ```bash
   git clone https://github.com/VinciYN/iHELPForAll.git
   ```
3. Créez une nouvelle branche pour vos modifications :
   ```bash
   git checkout -b ma-nouvelle-fonctionnalite
   ```
4. Une fois vos modifications terminées, envoyez une pull request !

---

## 📝 **Licence**

Ce projet est sous licence VXO/N2L/HLP. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

---

## 📧 **Contact**

Créateur : [VinciYN](https://github.com/VinciYN)  
Pour toute question ou suggestion, ouvrez une **Issue** dans ce dépôt.
