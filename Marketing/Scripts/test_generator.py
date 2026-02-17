
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Gen.generator import generate_post_image
from Marketing.Gen.caption_generator import generate_caption

def run_test():
    print("--- Démarrage du Test (Rougail Saucisse) ---")
    
    # 1. Génération de l'image
    print("1. Génération de l'image...")
    title = "MARDI SOIR : YERRES"
    subtitle = "🕕 18h00 - 21h00<br>🍛 Rougail Saucisse<br>🚚 Av. de la Grange" 
    
    # Path to the specific image requested
    bg_image = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Site Couleurs Péï/rougail-saucisse.png'))
    
    # TEST 1: POST
    print("Génération FORMAT POST...")
    generate_post_image(
        title="MARDI SOIR : YERRES", 
        subtitle="🕕 18h00 - 21h00<br>🍛 Rougail Saucisse<br>🚚 Av. de la Grange", 
        background_image_path=bg_image,
        output_filename="test_rougail_yerres_POST.png",
        format="post"
    )

    # TEST 2: STORY
    print("Génération FORMAT STORY...")
    generate_post_image(
        title="RETROUVEZ-MOI<br>CE SOIR", 
        subtitle="📍 YERRES<br>Avenue de la Grange<br>🕕 18h00 - 21h00", 
        background_image_path=bg_image,
        output_filename="test_rougail_yerres_STORY.png",
        format="story"
    )
    
    print("\n--- Test Terminé ---")

if __name__ == "__main__":
    run_test()
