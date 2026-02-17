
import os
import time
from playwright.sync_api import sync_playwright

# Auth state storage
AUTH_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'storage_state.json'))

def login_and_save_state():
    """
    Opens a browser for the user to log in manually, then saves the state.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        print("Opening Meta Business Suite...")
        page.goto("https://business.facebook.com/")
        
        print("Veuillez vous connecter manuellement dans la fenêtre du navigateur.")
        print("Une fois connecté et sur la page d'accueil, appuyez sur Entrée ici...")
        input("Appuyez sur Entrée pour sauvegarder la session...")
        
        context.storage_state(path=AUTH_FILE)
        print(f"Session sauvegardée dans {AUTH_FILE}")
        browser.close()

def publish_post(image_path, caption=None, is_story=False, schedule_date=None):
    """
    Simulates publishing or scheduling a post/story via Meta Business Suite.
    """
    if not os.path.exists(AUTH_FILE):
        print("❌ Erreur: Aucune session enregistrée. Lancez avec --setup d'abord.")
        return

    print(f"🚀 Lancement du navigateur pour {'STORY' if is_story else 'POST'}...")
    print(f"📅 Planification : {schedule_date.strftime('%d/%m/%Y à %H:%M') if schedule_date else 'IMMÉDIAT'}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=AUTH_FILE)
        page = context.new_page()
        
        print("Navigation vers Meta Business Suite...")
        # Direct link to specific composer if possible, otherwise generic
        page.goto("https://business.facebook.com/latest/composer")
        page.wait_for_timeout(5000) # Wait for load

        # Try to select Story mode
        if is_story:
            print("Tentative de bascule en mode STORY...")
            # Note: Selectors here are hypothetical and often change. 
            # We rely on text or user intervention for this demo.
            try:
                # Common pattern: click a button with text "Story" or "Reel"
                page.get_by_text("Story", exact=False).first.click(timeout=3000)
                page.wait_for_timeout(1000)
            except:
                print("⚠️ Impossible de basculer automatiquement en Story. Merci de vérifier.")

        # Upload Media
        print(f"Upload de l'image : {image_path}")
        try:
            # Generic file input locator
            page.set_input_files("input[type='file']", image_path)
            print("✅ Image uploadée (Si le sélecteur standard fonctionne).")
        except:
             print("⚠️ Échec de l'upload automatique. Copiez le chemin ci-dessous pour le faire manuellement :")
             print(image_path)

        # Handle Caption (Only for Posts usually, or text overlay for stories)
        if caption and not is_story:
            # Clipboard is safer for simple copy-paste
            print("📝 Texte copié dans le presse-papier (Simulation).")
            # page.evaluate(f"navigator.clipboard.writeText('{caption}')") 

        # Scheduling Info
        if schedule_date:
            print(f"\n🕒 MESSAGE POUR L'UTILISATEUR :")
            print(f"Veuillez régler la date sur : {schedule_date.strftime('%d/%m/%Y à %H:%M')}")
        
        print("\n🛑 HANDOVER : Le navigateur est ouvert. Validez les détails et cliquez sur 'Programmer'.")
        input("Appuyez sur Entrée dans ce terminal une fois la publication terminée pour fermer...")
        browser.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--setup', action='store_true', help='Run login setup')
    args = parser.parse_args()

    if args.setup:
        login_and_save_state()
    else:
        # Test with dummy data
        publish_post("dummy.png", "Ceci est un test.")
