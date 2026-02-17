
import os
import sys
import datetime
from datetime import timedelta

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Scripts.publisher import publish_post

def run_schedule_test():
    # 1. Calculate Date (Tomorrow 17:00)
    now = datetime.datetime.now()
    tomorrow = now + timedelta(days=1)
    schedule_time = tomorrow.replace(hour=17, minute=0, second=0, microsecond=0)
    
    print(f"--- Test de Planification ---")
    print(f"Cible : Demain ({schedule_time.strftime('%A %d')}) à 17h00")

    # 2. Define Assets
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SocialMedia/Posts/test_rougail_yerres_STORY.png'))
    
    # 3. Launch Publisher
    publish_post(
        image_path=image_path,
        caption="Retrouvez-nous ce soir à Yerres !",
        is_story=True,
        schedule_date=schedule_time
    )

if __name__ == "__main__":
    run_schedule_test()
