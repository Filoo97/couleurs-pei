
import os

import requests


def get_access_token():
    token = os.environ.get("META_USER_ACCESS_TOKEN")
    if not token:
        raise SystemExit("META_USER_ACCESS_TOKEN is required.")
    return token

def get_instagram_account_id():
    print("Test de la connexion API Meta...")
    access_token = get_access_token()
    
    # 1. Get User's Pages
    url = f"https://graph.facebook.com/v19.0/me/accounts?access_token={access_token}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"❌ Erreur API: {response.text}")
        return
    
    data = response.json()
    if 'data' not in data or len(data['data']) == 0:
        print("❌ Aucune Page Facebook trouvée liée à ce compte.")
        return

    print(f"✅ Pages trouvées : {len(data['data'])}")
    
    # 2. Find connected Instagram Account for each page
    for page in data['data']:
        page_name = page['name']
        page_id = page['id']
        print(f"\n🔍 Analyse de la page : {page_name} ({page_id})")
        
        url_ig = f"https://graph.facebook.com/v19.0/{page_id}?fields=instagram_business_account&access_token={access_token}"
        resp_ig = requests.get(url_ig)
        ig_data = resp_ig.json()
        
        if 'instagram_business_account' in ig_data:
            ig_id = ig_data['instagram_business_account']['id']
            print(f"   🎉 COMPTE INSTAGRAM TROUVÉ : ID = {ig_id}")
            print(f"   👉 À copier pour la config.")
        else:
            print("   ⚠️ Pas de compte Instagram Business lié à cette page.")

if __name__ == "__main__":
    get_instagram_account_id()
