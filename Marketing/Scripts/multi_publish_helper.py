
import os
import sys
from playwright.sync_api import sync_playwright

# Auth state storage
AUTH_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'storage_state.json'))
CAPTION_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SocialMedia/recap_caption.txt'))
IMAGE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SocialMedia/Posts/recap_semaine.png'))

def multi_publish():
    if not os.path.exists(AUTH_FILE):
        print("❌ Erreur: Aucune session enregistrée. Utilisez --setup.")
        return

    with open(CAPTION_FILE, 'r', encoding='utf-8') as f:
        caption = f.read()

    print("\n🦁 --- ASSISTANT DE PUBLICATION MULTI-CANAL --- 🦁")
    print("--------------------------------------------------")
    print(f"1. Instagram Feed + Facebook Page")
    print(f"2. Facebook Group: 'le groupe d'Yerres 91330'")
    print("--------------------------------------------------")

    with sync_playwright() as p:
        # We use headless=False so the user can see and interact
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=AUTH_FILE)
        
        # Tab 1: Meta Business Suite
        page1 = context.new_page()
        print("Ouverture de Meta Business Suite (Page + IG)...")
        page1.goto("https://business.facebook.com/latest/composer")
        
        # Tab 2: Facebook Group
        page2 = context.new_page()
        print("Recherche du groupe d'Yerres...")
        page2.goto("https://www.facebook.com/groups/search/groups_home/?q=le%20groupe%20d%27Yerres%2091330")

        print("\n📝 CAPTION (Copiée ci-dessous pour vous) :")
        print("------------------------------------------")
        print(caption)
        print("------------------------------------------")
        print("\nIMAGE : " + IMAGE_FILE)

        print("\n📥 ACTION REQUISE :")
        print("1. Dans l'onglet 1 (Business Suite) :")
        print("   - Sélectionnez Instagram et votre Page Facebook.")
        print("   - Collez le texte ci-dessus.")
        print("   - Ajoutez l'image (copiez le chemin ci-dessus).")
        print("   - Cliquez sur Publier.")
        print("2. Dans l'onglet 2 (Groupes) :")
        print("   - Allez sur le groupe 'le groupe d'Yerres 91330'.")
        print("   - Créez un nouveau post avec le texte et l'image.")
        
        print("\nAppuyez sur Entrée dans ce terminal une fois terminé pour fermer le navigateur.")
        input("Terminé ? ")
        browser.close()

if __name__ == "__main__":
    multi_publish()
