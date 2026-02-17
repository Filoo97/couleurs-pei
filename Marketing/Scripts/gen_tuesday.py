
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Gen.generator import generate_post_image

def generate_tuesday_story():
    # Assets
    bg_image = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Site Couleurs Péï/rougail-saucisse.png'))
    
    # Content
    title = "DEMAIN SOIR"
    subtitle = "📍 YERRES<br>Avenue de la Grange<br>🕕 18h00 - 21h00<br><br>🍛 Plats : Rougail Saucisse, Cari Poulet<br>🥟 Apéro : Samoussas, Bouchons, Bonbons Piment<br>🍰 Desserts : Gâteau Patate, Flan Coco"
    
    # Generate
    output = generate_post_image(
        title=title,
        subtitle=subtitle,
        background_image_path=bg_image,
        output_filename="story_mardi_yerres.png",
        format="story"
    )
    print(f"IMAGE_PATH:{output}")

if __name__ == "__main__":
    generate_tuesday_story()
