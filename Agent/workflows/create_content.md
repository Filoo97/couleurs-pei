# Workflow : Création de Contenu Interactif

Ce workflow utilise le script unifié `marketing_manager.py` pour piloter tout le processus.

1.  **Lancement**
    - Ouvrez un terminal :
    ```bash
    python Marketing/Scripts/marketing_manager.py
    ```

2.  **Configuration (Questions/Réponses)**
    - **Sujet** : Entrez le thème (ex: "Menu Mardi", "Soirée Spéciale").
    - **Format** : Choisissez `post` (carré) ou `story` (vertical).
    - **Détails** : Infos pour l'image (Lieu, Menu...).

3.  **Vérification Visuelle**
    - Le script génère l'image dans `Marketing/SocialMedia/Posts/`.
    - Allez voir le fichier (le chemin s'affiche) pour valider le design.

4.  **Rédaction**
    - Le script vous demande de saisir votre légende (Texte Instagram).
    - *Astuce : Vous pouvez utiliser ChatGPT à côté pour générer le texte et le coller ici.*

5.  **Décision : Publication ou Planification**
    - Le script vous pose la question cruciale :
        - `1` : **Publier tout de suite**.
        - `2` : **Planifier** (Format `JJ/MM/AAAA HH:MM`).
    - L'agent envoie ensuite les ordres à l'API Meta.
