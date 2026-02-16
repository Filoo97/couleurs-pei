import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Configuration
PAGE_ID = os.getenv("FB_PAGE_ID")
PAGE_TOKEN = os.getenv("FB_PAGE_TOKEN")
IG_ID = os.getenv("IG_BUSINESS_ID")

def post_to_facebook(message, image_url=None):
    """Publishes a post to the Facebook Page."""
    print(f"--- Publication Facebook en cours... ---")
    if image_url:
        url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/photos"
        payload = {
            "url": image_url,
            "caption": message,
            "access_token": PAGE_TOKEN
        }
    else:
        url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
        payload = {
            "message": message,
            "access_token": PAGE_TOKEN
        }
    
    response = requests.post(url, data=payload)
    result = response.json()
    
    if "id" in result:
        print(f"✅ Succès Facebook ! ID du post : {result['id']}")
    else:
        print(f"❌ Erreur Facebook : {result}")
    return result

def post_to_instagram(caption, image_url, story=False):
    """Publishes a photo to Instagram Feed or Story."""
    type_label = "STORY" if story else "FEED"
    print(f"--- Publication Instagram {type_label} en cours... ---")
    if not image_url:
        print("❌ Instagram nécessite obligatoirement une image.")
        return None

    # Étape 1 : Créer le conteneur média
    container_url = f"https://graph.facebook.com/v19.0/{IG_ID}/media"
    payload = {
        "image_url": image_url,
        "access_token": PAGE_TOKEN
    }
    
    if story:
        payload["media_type"] = "STORIES"
    else:
        payload["caption"] = caption # Les Stories ne supportent pas de légende via API

    response = requests.post(container_url, data=payload)
    result_json = response.json()
    container_id = result_json.get("id")
    
    if not container_id:
        print(f"❌ Erreur Création Conteneur IG : {result_json}")
        return result_json

    # Étape 2 : Publier le média
    publish_url = f"https://graph.facebook.com/v19.0/{IG_ID}/media_publish"
    publish_payload = {
        "creation_id": container_id,
        "access_token": PAGE_TOKEN
    }
    
    publish_response = requests.post(publish_url, data=publish_payload)
    result = publish_response.json()
    
    if "id" in result:
        print(f"✅ Succès Instagram {type_label} ! ID du média : {result['id']}")
    else:
        print(f"❌ Erreur Publication IG : {result}")
    return result

if __name__ == "__main__":
    import sys
    
    # Simple CLI handle: python expert_cm_couleurs_pei.py "Message" "URL_Image" [feed/story]
    message = sys.argv[1] if len(sys.argv) > 1 else "Test d'automatisation Couleurs Péï !"
    image = sys.argv[2] if len(sys.argv) > 2 else "https://couleurspei.fr/rougail-saucisse.png"
    mode = sys.argv[3].lower() if len(sys.argv) > 3 else "feed"
    
    is_story = (mode == "story")
    
    print(f"🚀 Démarrage de la publication automatique ({mode})...")
    
    if not is_story:
        post_to_facebook(message, image)
        post_to_instagram(message, image, story=False)
    else:
        # Les stories Facebook sont plus complexes via API, on se concentre sur IG Story
        post_to_instagram(message, image, story=True)
