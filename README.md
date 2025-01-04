# L'Importateur Radarr

Ce projet est un script Python permettant d'importer et de gérer des films dans Radarr à partir d'une source externe.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

1. **Python 3.6 ou version ultérieure**
2. **Pip** (gestionnaire de paquets pour Python)
3. Les dépendances mentionnées dans le fichier `requirements.txt` (si disponible) ou dans le script directement.
4. Un accès à l'API de votre instance Radarr avec les permissions nécessaires.

---

## Installation

### Étape 1 : Clonez le dépôt

Clonez ce dépôt GitHub dans le répertoire de votre choix :

```bash
git clone https://github.com/noxmoze/l-importateur-radarr.git
cd l-importateur-radarr
```

### Étape 2 : Installez les dépendances

Si le fichier `requirements.txt` est fourni :

```bash
pip install -r requirements.txt
```

Sinon, installez manuellement les bibliothèques nécessaires mentionnées dans le script. Par exemple :

```bash
pip install requests
```

---

## Configuration

Le script nécessite certains paramètres pour fonctionner correctement. Configurez ces paramètres directement dans le fichier `script.py` ou via un fichier de configuration externe si supporté.

### Paramètres requis

Dans le script, vous trouverez probablement des variables que vous devrez personnaliser, comme :

- **`RADARR_API_KEY`** : Clé API pour l'accès à Radarr.
- **`RADARR_URL`** : URL de votre instance Radarr (exemple : `http://localhost:7878`).
- **`SOURCE_PATH`** : Chemin vers les fichiers ou les données à importer.

Modifiez ces valeurs dans le script pour les adapter à votre configuration :

```python
RADARR_API_KEY = "votre_cle_api"
RADARR_URL = "http://localhost:7878"
SOURCE_PATH = "/chemin/vers/les/fichiers"
```

---

## Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python script.py
```

### Paramètres supplémentaires

Le script peut accepter des paramètres supplémentaires en ligne de commande. Consultez le code ou ajoutez une option d'aide pour plus de détails :

```bash
python script.py --help
```

### Fonctionnement général

1. Le script récupère les données des films à partir de `SOURCE_PATH`.
2. Il utilise l'API de Radarr pour vérifier si les films existent déjà.
3. Si un film n'existe pas, il est ajouté à Radarr avec les paramètres appropriés.

---

## Dépannage

### Problèmes fréquents

1. **Erreur de connexion à Radarr** :
   - Vérifiez que l'URL et la clé API sont correctes.
   - Assurez-vous que Radarr est en cours d'exécution et accessible depuis le réseau.

2. **Dépendances manquantes** :
   - Vérifiez que toutes les bibliothèques nécessaires sont installées.

3. **Permissions insuffisantes** :
   - Assurez-vous que le script a les droits nécessaires pour accéder aux fichiers et à l'API.
