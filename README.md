# l'importateur-radarr

Outils pour ajouter facilement une liste de films.

# Installation

Pour installer les dépendances :
``pip install requests``

# Configuration

Pour la configuration, il faut modifier plusieurs options.

- ``RADARR_URL`` = : remplacez "votre-instance-radarr.com" par l'URL de votre propre instance.
- ``API_KEY =`` : ajoutez votre clé API, que vous trouverez dans les réglages de votre compte Radarr.
- ``CHEMIN_BIBLIOTHEQUE =`` : modifiez le chemin par celui configuré dans votre Radarr.
- ``QUALITE_PROFIL`` : remplacez le 0 par l'ID du profil que vous souhaitez utiliser pour le choix des fichiers.

# Utilisation

Pour l'utilisation, commencez par créer un fichier films.txt. Ce fichier doit contenir tous les films que Radarr doit traiter.
Une fois le fichier créé et rempli, vous pouvez démarrer le script avec les commandes suivantes :
Pour Linux :
``python script.py``

Pour Windows :
``py script.py``
