
import os
import sys
import datetime
from datetime import datetime as dt

# Add project root to sys.path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Gen.generator import generate_post_image
from Marketing.Scripts.publish_api import publish_media
from Marketing.Scripts.culture_data import EXPRESSIONS, HISTOIRE, CUISINE
import random

def get_user_input(prompt, default=None):
    if default:
        user_input = input(f"{prompt} [{default}]: ")
        return user_input if user_input.strip() else default
    return input(f"{prompt}: ")

def main():
    print("\n🦁 --- COULEURS PÉÏ COMMUNITY MANAGER --- 🦁")
    print("---------------------------------------------")

    print("\n📋 Type de Contenu :")
    print("1. Menu / Planning (Utilité)")
    print("2. L'Instant Kréol (Expression)")
    print("3. L'Histoire du Péï (Anecdote)")
    print("4. Secret de Cuisine (Ingrédient)")
    print("5. Autre (Libre)")
    
    type_choice = get_user_input("Votre choix", "1")
    
    topic = ""
    location_details = ""
    bg_image_name = "rougail-saucisse.png"
    format_choice = "story"
    theme = ""

    if type_choice == "2":
        # Instant Kréol logic
        data = random.choice(EXPRESSIONS)
        phrase = get_user_input("Expression Créole", data["phrase"])
        definition = get_user_input("Signification", data["definition"])
        example = get_user_input("Exemple", data["example"])
        
        topic = "L'INSTANT KRÉOL 🇷🇪"
        location_details = (
            f"<span style='font-size: 3rem; color: #ba9669;'>\"{phrase}\"</span><br><br>"
            f"<b>Signification :</b> {definition}<br><br>"
            f"<i>\"{example}\"</i>"
        )
        theme = "theme-elegant"
        format_choice = "story"

    elif type_choice == "3":
        # History logic
        data = random.choice(HISTOIRE)
        h_title = get_user_input("Titre de l'anecdote", data["title"])
        h_text = get_user_input("Texte de l'anecdote", data["text"])
        
        topic = "L'HISTOIRE DU PÉÏ 📜"
        location_details = (
            f"<span style='font-size: 2.5rem; color: #ba9669;'>{h_title}</span><br><br>"
            f"<div style='text-align: justify;'>{h_text}</div>"
        )
        theme = "theme-elegant"
        format_choice = "story"

    elif type_choice == "4":
        # Cuisine logic
        data = random.choice(CUISINE)
        ingredient = get_user_input("L'ingrédient", data["ingredient"])
        secret = get_user_input("Le secret", data["secret"])
        
        topic = "SECRET DE CUISINE 🍛"
        location_details = (
            f"<span style='font-size: 3rem; color: #ba9669;'>Le {ingredient}</span><br><br>"
            f"<div style='text-align: center;'>{secret}</div>"
        )
        theme = "theme-elegant"
        format_choice = "story"

    elif type_choice == "5":
        topic = get_user_input("Sujet", "Titre du Post")
        location_details = get_user_input("Texte sur l'image", "Description")
        format_choice = get_user_input("Format (post/story)", "story").lower()
    else:
        # Default Menu logic
        topic = get_user_input("Sujet du post (ex: Menu Mardi, Promo)", "Menu du Jour")
        location_details = get_user_input("Détails Lieu/Menu (pour l'image)", "Voir sur place")
        format_choice = get_user_input("Format (post/story)", "story").lower()

    is_story = format_choice == "story"
    theme = "theme-elegant" if type_choice == "2" else ""

    # 2. Génération Visuelle
    print("\n🎨 Génération du visuel en cours...")
    
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_{timestamp}_{format_choice}.png"
    
    # Only set bg_image if not in elegant theme or if explicitly provided
    bg_image = None
    if theme != "theme-elegant":
        bg_image = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../Site Couleurs Péï/{bg_image_name}'))
    
    output_path = generate_post_image(
        title=topic.upper(),
        subtitle=location_details,
        background_image_path=bg_image,
        output_filename=filename,
        format=format_choice,
        theme=theme
    )
    
    print(f"✅ Image générée : {output_path}")
    
    # 3. Rédaction Légende
    print("\n✍️ Rédaction de la légende")
    default_caption = f"Retrouvez-nous pour un délicieux {topic} ! #CouleursPei #Reunion"
    if type_choice == "2":
        default_caption = f"Oté la famille ! 👋 On se retrouve pour l'Instant Kréol ! 🇷🇪\n\nConnaissiez-vous cette expression ?\n\n#CouleursPei #Culture #Reunion #InstantKreol"
    
    caption = get_user_input("Texte du post (Légende Instagram)", default_caption)

    # ... (rest of the logic for publication) ...
    # 4. Décision Publication
    print("\n🚀 Options de Publication")
    print("1. Publier MAINTENANT")
    print("2. Planifier pour plus tard")
    print("3. Annuler")
    
    choice = get_user_input("Votre choix", "3")
    
    schedule_time = None
    
    if choice == "3":
        print("❌ Opération annulée.")
        return

    if choice == "2":
        date_str = get_user_input("Date et Heure (format JJ/MM/AAAA HH:MM)", "17/02/2026 17:00")
        try:
            schedule_time = dt.strptime(date_str, "%d/%m/%Y %H:%M")
            if schedule_time < dt.now():
                print("⚠️ Attention : La date est dans le passé.")
        except ValueError:
            print("❌ Format de date invalide.")
            return

    # 5. Exécution
    print("\n⏳ Traitement en cours...")
    publish_media(
        image_path=output_path,
        caption=caption,
        is_story=is_story,
        schedule_time=schedule_time
    )

if __name__ == "__main__":
    main()
