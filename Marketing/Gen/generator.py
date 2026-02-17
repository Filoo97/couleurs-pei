
import os
from playwright.sync_api import sync_playwright
import sys

# Add project root to sys.path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Marketing.Assets.brand_assets import BrandAssets

TEMPLATE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Templates/post_template.html'))
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SocialMedia/Posts'))

def generate_post_image(title, subtitle, background_image_path=None, output_filename="post_output.png", format="post", theme=""):
    """
    Generates a social media image (Post or Story).
    format: "post" (1080x1080) or "story" (1080x1920)
    theme: "theme-elegant" or empty
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Calculate absolute paths for assets
    site_assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Site Couleurs Péï'))
    logo_path = os.path.join(site_assets_dir, 'logo.png').replace(os.sep, '/')
    css_path = os.path.join(site_assets_dir, 'style.css').replace(os.sep, '/')
    
    # Prepare Image Path
    if background_image_path:
        bg_url = f"file:///{background_image_path.replace(os.sep, '/')}"
    else:
        # Fallback to a default if not using a special theme, or leave empty for CSS-only
        if theme == "theme-elegant":
            bg_url = ""
        else:
            bg_url = f"file:///{os.path.join(site_assets_dir, 'Photo_Menu_Hero.png').replace(os.sep, '/')}"

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Replace placeholders
    html_content = html_content.replace('REPLACE_TITLE', title)
    html_content = html_content.replace('REPLACE_SUBTITLE', subtitle)
    html_content = html_content.replace('PHONE_IMAGE_URL', bg_url)
    
    # Replace relative paths with absolute file URLs
    html_content = html_content.replace('../../Site Couleurs Péï/style.css', f'file:///{css_path}')
    html_content = html_content.replace('../../Site Couleurs Péï/logo.png', f'file:///{logo_path}')
    
    # Inject format AND theme classes
    body_classes = f"format-{format} {theme}".strip()
    html_content = html_content.replace('class="REPLACE_THEME"', f'class="{body_classes}"')

    # Create a temporary HTML file to render
    temp_html_path = os.path.join(OUTPUT_DIR, 'temp_render.html')
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generating {format} image for: {title}")
    
    # Define Viewport based on format
    if format == "story":
        width, height = 1080, 1920
    else:
        width, height = 1080, 1080

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': width, 'height': height})
        
        # Load the local HTML file
        page.goto(f"file:///{temp_html_path}")
        
        # Wait for fonts/images to load
        page.wait_for_timeout(1000)
        
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        page.screenshot(path=output_path)
        print(f"Image saved to: {output_path}")
        
        browser.close()

    # Cleanup temp file
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
        
    return output_path

if __name__ == "__main__":
    generate_post_image(
        title="MENU DU JOUR",
        subtitle="Rougail Saucisse & Cari Poulet au programme !",
        output_filename="test_post.png"
    )
