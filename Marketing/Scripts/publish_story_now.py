
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Scripts.publish_api import publish_media

def publish_story_immediate():
    # 1. Image
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SocialMedia/Posts/story_mardi_yerres.png'))
    
    # 2. Publish NOW
    caption = "Rougail Saucisse & Cari Poulet ce mardi soir à Yerres ! 🇷🇪 #CouleursPei #Yerres #FoodTruck"
    
    print(f"--- PUBLICATION IMMEDIATE (Via Tâche Planifiée) ---")
    
    publish_media(
        image_path=image_path,
        caption=caption,
        is_story=True,
        schedule_time=None # Force immediate publish
    )

if __name__ == "__main__":
    publish_story_immediate()
