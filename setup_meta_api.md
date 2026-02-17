# Guide de Configuration : API Meta pour l'Automatisation

Pour que votre agent puisse publier automatiquement sur Instagram et Facebook, nous devons configurer une application sur le portail développeur de Meta.

## Étape 1 : Créer une App Meta
1.  Allez sur [developers.facebook.com](https://developers.facebook.com/).
2.  Cliquez sur **"My Apps"** (Mes Apps) > **"Create App"**.
3.  Sélectionnez **"Other"** (Autre) > **"Business"**.
4.  Donnez un nom (ex: "Couleurs Péï Agent").
5.  Associez votre **Business Manager** si vous en avez un (recommandé).

## Étape 2 : Ajouter Instagram Graph API
1.  Dans le tableau de bord de l'app, trouvez **"Instagram Graph API"** et cliquez sur **"Set up"**.
2.  Allez dans **"Settings"** > **"Basic"**.
3.  Notez votre **App ID** et **App Secret**.

## Étape 3 : Générer un Access Token
1.  Allez dans **"Tools"** > **"Graph API Explorer"**.
2.  Selectionnez votre App.
3.  Ajoutez les permissions suivantes dans "Add a Permission" :
    - `instagram_basic`
    - `instagram_content_publish`
    - `pages_show_list`
    - `pages_read_engagement` (pour lire les commentaires plus tard)
4.  Cliquez sur **"Generate Access Token"**.
5.  Important : Ce token est temporaire (1h). Pour un usage long terme, nous l'échangerons contre un token longue durée via le script.

## Étape 4 : ID du Compte Instagram Business
1.  Dans l'explorateur Graph API, faites une requête `GET` sur :
    `me/accounts`
2.  Trouvez la Page Facebook liée à votre Instagram. Notez son ID.
3.  Faites une requête `GET` sur :
    `{PAGE_ID}?fields=instagram_business_account`
4.  L'ID qui s'affiche est votre **INSTAGRAM_ACCOUNT_ID**.

---
## Résumé des infos à me fournir :
- **ACCESS_TOKEN** (Celui généré à l'étape 3)
- **INSTAGRAM_ACCOUNT_ID** (Celui trouvé à l'étape 4)
