
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Gen.generator import generate_post_image

def generate_kreol_moment(phrase, definition, example):
    # Content
    title = "L'INSTANT KRÉOL 🇷🇪"
    
    # Subtitle with specific formatting
    subtitle = (
        f"<span style='font-size: 3rem; color: #ba9669;'>\"{phrase}\"</span><br><br>"
        f"<b>Signification :</b> {definition}<br><br>"
        f"<i>\"{example}\"</i>"
    )
    
    output_filename = f"instant_kreol_{phrase.lower().replace(' ', '_')}.png"
    
    # Generate as Story with the Elegant Theme
    output = generate_post_image(
        title=title,
        subtitle=subtitle,
        background_image_path=None, # Use CSS theme instead
        output_filename=output_filename,
        format="story",
        theme="theme-elegant"
    )
def generate_history_moment(anecdote_title, anecdote_text):
    # Content
    title = "L'HISTOIRE DU PÉÏ 📜"
    
    subtitle = (
        f"<span style='font-size: 2.5rem; color: #ba9669;'>{anecdote_title}</span><br><br>"
        f"<div style='text-align: justify;'>{anecdote_text}</div>"
    )
    
    filename_id = anecdote_title.lower().replace(' ', '_')[:20]
    output_filename = f"histoire_{filename_id}.png"
    
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

def generate_cuisine_moment(ingredient, secret, bg_image=None):
    # Content
    title = "SECRET DE CUISINE 🍛"
    
    subtitle = (
        f"<span style='font-size: 3.5rem; color: #ba9669;'>Le {ingredient}</span><br><br>"
        f"<div style='text-align: center;'>{secret}</div>"
    )
    
    filename_id = ingredient.lower().replace(' ', '_')[:20]
    output_filename = f"cuisine_{filename_id}.png"
    
    output = generate_post_image(
        title=title,
        subtitle=subtitle,
        background_image_path=bg_image,
        output_filename=output_filename,
        format="story",
        theme="theme-elegant"
    )
    print(f"IMAGE_PATH:{output}")
    return output

if __name__ == "__main__":
    # Example 1: Oté !
    generate_kreol_moment(
        phrase="Oté !",
        definition="L'interjection la plus célèbre de la Réunion ! Elle exprime la surprise, l'admiration ou ponctue simplement une phrase. C'est le 'Oh là là' kréol.",
        example="Oté ! Regarde la taille du cari que Couleurs Péï a préparé !"
    )

    # Example 2: History
    generate_history_moment(
        anecdote_title="Le Piton de la Fournaise",
        anecdote_text="L'un des volcans les plus actifs de la planète ! Saviez-vous qu'il entre en éruption en moyenne tous les 9 mois ? C'est le cœur battant de notre île intense."
    )

    # Example 3: Cuisine
    bg_combava = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Site Couleurs Péï/cari-thon-combava.png'))
    generate_cuisine_moment(
        ingredient="Combava",
        secret="On ne mange pas le fruit ! C'est son zeste, râpé finement, qui donne ce parfum citronné et puissant incomparable à nos caris.",
        bg_image=bg_combava
    )
