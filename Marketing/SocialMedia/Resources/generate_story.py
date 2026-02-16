import os
from PIL import Image, ImageDraw, ImageFont

def generate_social_story(background_path, logo_path, output_path, day_text, location_text, time_text):
    # Dimensions Story Instagram (Vertical)
    size = (1080, 1920)
    
    GOLD = (186, 150, 105) # #ba9669
    NAVY = (44, 58, 81)    # #2c3a51
    WHITE = (255, 255, 255)
    
    if not os.path.exists(background_path):
        print(f"Erreur: Image non trouvée {background_path}")
        return
    
    bg = Image.open(background_path).convert("RGBA")
    
    # Redimensionnement intelligent pour remplir la hauteur
    width, height = bg.size
    target_ratio = size[0] / size[1]
    current_ratio = width / height
    
    if current_ratio > target_ratio:
        new_width = int(height * target_ratio)
        left = (width - new_width) / 2
        bg = bg.crop((left, 0, left + new_width, height))
    else:
        new_height = int(width / target_ratio)
        top = (height - new_height) / 2
        bg = bg.crop((0, top, width, top + new_height))
    
    bg = bg.resize(size, Image.LANCZOS)
    
    # Overlay sombre global
    overlay = Image.new('RGBA', size, (0, 0, 0, 60))
    bg = Image.alpha_composite(bg, overlay)
    
    draw = ImageDraw.Draw(bg)
    
    # Logo en haut au centre
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo.thumbnail((300, 300), Image.LANCZOS)
        bg.paste(logo, (int((size[0] - logo.size[0]) / 2), 150), logo)
    
    # Bandeau bleu (Positionné plus bas : box_y à 1100)
    box_y = 1100
    box_h = 450
    draw.rectangle([50, box_y, size[0]-50, box_y + box_h], fill=NAVY)
    draw.rectangle([50, box_y, size[0]-50, box_y + 10], fill=GOLD) 
    draw.rectangle([50, box_y + box_h - 10, size[0]-50, box_y + box_h], fill=GOLD) 

    # Polices adaptatives
    try:
        # On commence à 80 et on réduit si ça dépasse
        font_size = 75
        font_main = ImageFont.truetype("arialbd.ttf", font_size)
        
        # Vérification largeur max (980px car box fait 1080-100)
        day_bbox = draw.textbbox((0, 0), day_text, font=font_main)
        text_w = day_bbox[2] - day_bbox[0]
        while text_w > 900 and font_size > 40:
            font_size -= 5
            font_main = ImageFont.truetype("arialbd.ttf", font_size)
            day_bbox = draw.textbbox((0, 0), day_text, font=font_main)
            text_w = day_bbox[2] - day_bbox[0]

        font_sub = ImageFont.truetype("arial.ttf", 50)
        font_emoji = ImageFont.truetype("seguiemj.ttf", 45)
    except:
        font_main = font_sub = font_emoji = ImageFont.load_default()

    # Textes
    # "RETROUVEZ-MOI CE SOIR"
    day_bbox = draw.textbbox((0, 0), day_text, font=font_main)
    draw.text(((size[0] - (day_bbox[2]-day_bbox[0]))/2, box_y + 90), day_text, font=font_main, fill=GOLD)
    
    # LIEU avec 📍
    pin_icon = "📍"
    pin_bbox = draw.textbbox((0, 0), pin_icon, font=font_emoji)
    loc_bbox = draw.textbbox((0, 0), location_text, font=font_sub)
    total_loc_w = (pin_bbox[2]-pin_bbox[0]) + 15 + (loc_bbox[2]-loc_bbox[0])
    start_x = (size[0] - total_loc_w) / 2
    
    draw.text((start_x, box_y + 225), pin_icon, font=font_emoji, fill=WHITE, embedded_color=True)
    draw.text((start_x + (pin_bbox[2]-pin_bbox[0]) + 15, box_y + 220), location_text, font=font_sub, fill=WHITE)
    
    # HORAIRE avec ⏰
    clock_icon = "⏰"
    clock_bbox = draw.textbbox((0, 0), clock_icon, font=font_emoji)
    time_bbox = draw.textbbox((0, 0), time_text, font=font_sub)
    total_time_w = (clock_bbox[2]-clock_bbox[0]) + 15 + (time_bbox[2]-time_bbox[0])
    start_x_time = (size[0] - total_time_w) / 2
    
    draw.text((start_x_time, box_y + 325), clock_icon, font=font_emoji, fill=GOLD, embedded_color=True)
    draw.text((start_x_time + (clock_bbox[2]-clock_bbox[0]) + 15, box_y + 320), time_text, font=font_sub, fill=GOLD)

    # Sauvegarde
    bg.save(output_path, "PNG")
    print(f"✅ Story mise à jour (texte ajusté) : {output_path}")

if __name__ == "__main__":
    res_path = os.path.join("Marketing", "SocialMedia", "Resources")
    out_path = os.path.join("Marketing", "SocialMedia", "Stories", "story_mardi_yerres.png")
    generate_social_story(
        background_path=os.path.join(res_path, "rougail-saucisse.png"),
        logo_path=os.path.join(res_path, "logo.png"),
        output_path=out_path,
        day_text="RETROUVEZ-MOI CE SOIR",
        location_text="YERRES - Avenue de la Grange",
        time_text="18H00 - 21H00"
    )
