
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Gen.generator import generate_post_image

def generate_weekly_recap():
    # Assets
    bg_image = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Site Couleurs Péï/Photo_Menu_Hero.png'))
    
    # Content
    title = "PROGRAMME DE LA SEMAINE"
    
    # Constructing a rich subtitle
    subtitle = (
        "📍 PLANNING DE LA SEMAINE :<br>"
        "• MARDI SOIR : Yerres, Av. de la Grange (18h-21h)<br>"
        "• MERCREDI MIDI : Yerres, Parvis du CEC (11h45-14h)<br>"
        "• MERCREDI SOIR : Brunoy, Parvis de la Gare (18h-21h)<br>"
        "• JEUDI MIDI : Clinique de Longjumeau (11h45-14h)<br>"
        "• VENDREDI MIDI : Hôpital Privé du Val d'Yerres (11h45-14h)<br><br>"
        "🍛 AU MENU :<br>"
        "• Plats : Rougail Saucisse, Cari Poulet, Rougail Morue<br>"
        "• Apéro : Bouchons, Samoussas, Bonbon Piment<br>"
        "• Desserts : Gâteau Patate, Flan Coco"
    )
    
    # Generate as Story (more vertical space for many lines)
    output = generate_post_image(
        title=title,
        subtitle=subtitle,
        background_image_path=bg_image,
        output_filename="recap_semaine.png",
        format="story"
    )
    print(f"IMAGE_PATH:{output}")

if __name__ == "__main__":
    generate_weekly_recap()
