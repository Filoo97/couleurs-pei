
import requests
import os
import argparse
import datetime
import sys

# --- CONFIGURATION ---
INSTAGRAM_ACCOUNT_ID = "17841429117751312"
GRAPH_URL = "https://graph.facebook.com/v19.0"


def get_access_token():
    token = os.environ.get("META_INSTAGRAM_ACCESS_TOKEN")
    if not token:
        raise SystemExit("META_INSTAGRAM_ACCESS_TOKEN is required.")
    return token

def upload_temp_image(image_path):
    """
    Uploads the image to tmpfiles.org to get a temporary public URL.
    Returns the direct download URL.
    """
    print("   ☁️ Upload temporaire de l'image (tmpfiles.org)...")
    url = "https://tmpfiles.org/api/v1/upload"
    
    try:
        files = {'file': open(image_path, 'rb')}
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            data = response.json()
            # Convert to direct URL (replace 'tmpfiles.org/' with 'tmpfiles.org/dl/')
            url_obj = data['data']['url']
            direct_url = url_obj.replace('tmpfiles.org/', 'tmpfiles.org/dl/')
            print(f"   ✅ Image en ligne : {direct_url}")
            return direct_url
        else:
            print(f"   ❌ Erreur upload temporaire : {response.text}")
            return None
    except Exception as e:
        print(f"   ❌ Exception upload : {e}")
        return None

def publish_media(image_path, caption, is_story=False, schedule_time=None):
    """
    Publishes an image to Instagram via Meta Graph API.
    """
    print("\n🚀 PUBLICATION VIA API META")
    print("--------------------------------")
    
    if not os.path.exists(image_path):
        print(f"❌ Image introuvable : {image_path}")
        return

    access_token = get_access_token()

    # 1. Upload to Temporary Host
    image_url = upload_temp_image(image_path)
    if not image_url:
        return
    
    # Step 2: Create Container
    print(f"\n1. Création du Conteneur {'STORY' if is_story else 'POST'}...")
    url_container = f"{GRAPH_URL}/{INSTAGRAM_ACCOUNT_ID}/media"
    
    payload = {
        'image_url': image_url,
        'caption': caption,
        'access_token': access_token
    }
    
    if is_story:
        payload['media_type'] = 'STORIES'
    
    if schedule_time:
        # Convert to Unix Timestamp
        ts = int(schedule_time.timestamp())
        payload['scheduled_publish_time'] = ts
        payload['published'] = 'false'
        print(f"   📅 Planification demandée : {schedule_time} (TS: {ts})")
    
    # API CALL
    response = requests.post(url_container, data=payload)
    
    if response.status_code == 200:
        container_id = response.json()['id']
        print(f"   ✅ Conteneur créé ID: {container_id}")
    else:
        print(f"   ❌ Erreur création conteneur : {response.text}")
        return

    # Step 3: Publish Container
    # NOTE: For scheduling, we MUST also call media_publish to "commit" the schedule.
    # The API will see the 'scheduled_publish_time' in the container and put it in the schedule queue.
    
    print(f"\n2. Publication/Planification du Conteneur {container_id}...")
    url_publish = f"{GRAPH_URL}/{INSTAGRAM_ACCOUNT_ID}/media_publish"
    payload_pub = {
        'creation_id': container_id,
        'access_token': access_token
    }
    
    response_pub = requests.post(url_publish, data=payload_pub)
    
    if response_pub.status_code == 200:
        if schedule_time:
             print(f"   ✅ PLANIFICATION RÉUSSIE ! Le post est programmé pour {schedule_time}.")
             print(f"   ID: {response_pub.json()['id']}")
        else:
             print(f"   ✅ PUBLICATION RÉUSSIE ! ID: {response_pub.json()['id']}")
    else:
        print(f"   ❌ Erreur publication : {response_pub.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Publish media to Instagram.')
    parser.add_argument('--image', type=str, required=True, help='Path to the image file.')
    parser.add_argument('--caption', type=str, default='', help='Caption for the post.')
    parser.add_argument('--story', action='store_true', help='Publish as a Story.')
    parser.add_argument('--schedule', type=str, help='Schedule time (format: DD/MM/YYYY HH:MM)')
    
    args = parser.parse_args()
    
    schedule_time = None
    if args.schedule:
        try:
            schedule_time = datetime.datetime.strptime(args.schedule, "%d/%m/%Y %H:%M")
        except ValueError:
            print("❌ Format de date invalide pour --schedule (attendu: JJ/MM/AAAA HH:MM)")
            sys.exit(1)
            
    publish_media(
        image_path=os.path.abspath(args.image),
        caption=args.caption,
        is_story=args.story,
        schedule_time=schedule_time
    )
