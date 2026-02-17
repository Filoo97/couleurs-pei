
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Gen.generator import generate_post_image

def generate_announcement():
    # Content
    title = "DU NOUVEAU ICI ! 🌋"
    
    # Subtitle for announcement
    subtitle = (
        "Préparez-vous à voyager... ✨<br><br>"
        "Nous allons désormais partager régulièrement avec vous les secrets, "
        "l'histoire et l'humour de notre belle île de la Réunion.<br><br>"
        "<b>Restez connectés ! 🇷🇪</b>"
    )
    
    output_filename = "annonce_nouvelle_ligne.png"
    
    # Generate as Story (more impact for an announcement)
    output = generate_post_image(
        title=title,
        subtitle=subtitle,
        background_image_path=None,
        output_filename=output_filename,
        format="story",
        theme="theme-elegant"
    )
    print(f"IMAGE_PATH:{output}")
    return output

if __name__ == "__main__":
    generate_announcement()
