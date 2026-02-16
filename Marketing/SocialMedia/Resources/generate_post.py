import os
from PIL import Image, ImageDraw, ImageFont

def generate_social_post(background_path, logo_path, output_path, day_text, location_text, time_text):
    # Dimensions standard
    size = (1080, 1080)
    
    # Couleurs de la charte
    GOLD = (186, 150, 105) # #ba9669
    NAVY = (44, 58, 81)    # #2c3a51
    WHITE = (255, 255, 255)
    
    # 1. Charger et préparer le fond
    if not os.path.exists(background_path):
        print(f"Erreur: Image de fond non trouvée {background_path}")
        return
    
    bg = Image.open(background_path).convert("RGBA")
    
    # Crop to square
    width, height = bg.size
    min_dim = min(width, height)
    left = (width - min_dim)/2
    top = (height - min_dim)/2
    right = (width + min_dim)/2
    bottom = (height + min_dim)/2
    bg = bg.crop((left, top, right, bottom))
    bg = bg.resize(size, Image.LANCZOS)
    
    # Assombrir légèrement
    overlay = Image.new('RGBA', size, (0, 0, 0, 40))
    bg = Image.alpha_composite(bg, overlay)
    
    # 2. Bandeau
    draw = ImageDraw.Draw(bg)
    banner_height = 250
    draw.rectangle([0, size[1] - banner_height, size[0], size[1]], fill=NAVY)
    draw.rectangle([0, size[1] - banner_height, size[0], size[1] - banner_height + 8], fill=GOLD)
    
    # 3. Logo
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo.thumbnail((180, 180), Image.LANCZOS)
        bg.paste(logo, (size[0] - logo.size[0] - 40, 40), logo)
    
    # 4. Polices
    try:
        font_bold = ImageFont.truetype("arialbd.ttf", 80)
        font_regular = ImageFont.truetype("arial.ttf", 40)
        # Font pour les emojis sur Windows
        font_emoji = ImageFont.truetype("seguiemj.ttf", 35)
    except:
        font_bold = ImageFont.load_default()
        font_regular = ImageFont.load_default()
        font_emoji = ImageFont.load_default()
        
    # Dessiner "JOUR"
    day_bbox = draw.textbbox((0, 0), day_text, font=font_bold)
    day_w = day_bbox[2] - day_bbox[0]
    draw.text(((size[0] - day_w) / 2, size[1] - banner_height + 40), day_text, font=font_bold, fill=GOLD)
    
    # Dessiner "LIEU" avec icône 📍
    pin_icon = "📍"
    loc_text_full = f"{location_text}"
    
    # On calcule la largeur totale (icône + texte)
    pin_bbox = draw.textbbox((0, 0), pin_icon, font=font_emoji)
    loc_bbox = draw.textbbox((0, 0), loc_text_full, font=font_regular)
    
    total_loc_w = (pin_bbox[2] - pin_bbox[0]) + 15 + (loc_bbox[2] - loc_bbox[0])
    start_x = (size[0] - total_loc_w) / 2
    y_loc = size[1] - banner_height + 140
    
    # Dessiner l'émoji (en blanc ou couleur d'origine)
    draw.text((start_x, y_loc + 5), pin_icon, font=font_emoji, fill=WHITE, embedded_color=True)
    # Dessiner le texte
    draw.text((start_x + (pin_bbox[2] - pin_bbox[0]) + 15, y_loc), loc_text_full, font=font_regular, fill=WHITE)
    
    # Dessiner "HORAIRE" avec icône ⏰
    clock_icon = "⏰"
    time_text_full = f"{time_text}"
    
    clock_bbox = draw.textbbox((0, 0), clock_icon, font=font_emoji)
    time_bbox = draw.textbbox((0, 0), time_text_full, font=font_regular)
    
    total_time_w = (clock_bbox[2] - clock_bbox[0]) + 15 + (time_bbox[2] - time_bbox[0])
    start_x_time = (size[0] - total_time_w) / 2
    y_time = size[1] - banner_height + 195
    
    draw.text((start_x_time, y_time + 5), clock_icon, font=font_emoji, fill=GOLD, embedded_color=True)
    draw.text((start_x_time + (clock_bbox[2] - clock_bbox[0]) + 15, y_time), time_text_full, font=font_regular, fill=GOLD)
    
    # Sauvegarder
    bg.save(output_path, "PNG")
    print(f"✅ Image générée avec émojis : {output_path}")

if __name__ == "__main__":
    import os
    res_path = os.path.join("Marketing", "SocialMedia", "Resources")
    out_path = os.path.join("Marketing", "SocialMedia", "Posts", "post_mardi_yerres.png")
    
    generate_social_post(
        background_path=os.path.join(res_path, "rougail-saucisse.png"),
        logo_path=os.path.join(res_path, "logo.png"),
        output_path=out_path,
        day_text="MARDI SOIR",
        location_text="YERRES - Avenue de la Grange",
        time_text="18h00 - 21h00"
    )
