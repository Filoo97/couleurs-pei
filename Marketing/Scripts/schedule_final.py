
import os
import sys
import datetime

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Scripts.publish_api import publish_media

def schedule_story():
    # 1. Image
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SocialMedia/Posts/story_mardi_yerres.png'))
    
    # 2. Date: Tomorrow (Tuesday 17th) at 17:00
    # Note: If today is Monday 16th, tomorrow is 17th.
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    schedule_time = tomorrow.replace(hour=17, minute=0, second=0, microsecond=0)
    
    print(f"--- Planification Finale ---")
    print(f"Cible : {schedule_time.strftime('%A %d/%m/%Y à %H:%M')}")
    
    # 3. Publish
    caption = "Rougail Saucisse & Cari Poulet ce mardi soir à Yerres ! 🇷🇪 #CouleursPei #Yerres #FoodTruck"
    
    publish_media(
        image_path=image_path,
        caption=caption,
        is_story=True,
        schedule_time=schedule_time
    )

if __name__ == "__main__":
    schedule_story()
