import requests
import json

# Configuration
RADARR_URL = "http://votre-instance-radarr.com/api/v3"
API_KEY = "votre-cle-api"
FILM_LISTE = "films.txt"
CHEMIN_BIBLIOTHEQUE = "/chemin/vers/votre/bibliotheque"
QUALITE_PROFIL = 0  # ID du profil de qualité dans Radarr
SCAN_IMMEDIAT = True
MONITORER = True


def ajouter_film(titre):
    """
    Ajoute un film à Radarr en utilisant le titre fourni.
    """
    recherche_url = f"{RADARR_URL}/movie/lookup"
    ajout_url = f"{RADARR_URL}/movie"

    headers = {
        "X-Api-Key": API_KEY,
        "Content-Type": "application/json"
    }

    # Rechercher le film par titre
    response = requests.get(recherche_url, params={"term": titre}, headers=headers)

    if response.status_code != 200:
        print(f"Erreur lors de la recherche du film '{titre}': {response.status_code}")
        return

    resultats = response.json()
    if not resultats:
        print(f"Aucun résultat trouvé pour '{titre}'.")
        return

    # Utiliser le premier résultat pour ajouter le film
    film_data = resultats[0]
    payload = {
        "title": film_data["title"],
        "qualityProfileId": QUALITE_PROFIL["id"],
        "languageProfileId": 0,  # ID par défaut pour "Any"
        "year": film_data["year"],
        "tmdbId": film_data["tmdbId"],
        "rootFolderPath": CHEMIN_BIBLIOTHEQUE,
        "monitored": MONITORER,
        "addOptions": {
            "searchForMovie": SCAN_IMMEDIAT
        }
    }

    response = requests.post(ajout_url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Film ajouté avec succès : {film_data['title']} ({film_data['year']})")
        print(f"Profil de qualité utilisé : {QUALITE_PROFIL['nom']}")
    elif response.status_code == 400:
        print(f"Le film '{film_data['title']}' est déjà présent dans Radarr.")
    else:
        print(f"Erreur lors de l'ajout de '{film_data['title']}': {response.status_code}")


def ajouter_films_depuis_fichier(fichier):
    """
    Lit un fichier texte et ajoute chaque film à Radarr.
    """
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            titres = [ligne.strip() for ligne in f if ligne.strip()]

        for titre in titres:
            ajouter_film(titre)
    except FileNotFoundError:
        print(f"Fichier introuvable : {fichier}")
    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {str(e)}")


# Lancer le script
if __name__ == "__main__":
    ajouter_films_depuis_fichier(FILM_LISTE)
