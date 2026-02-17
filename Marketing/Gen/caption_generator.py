
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


# PERSONA_PATH is defined below


PERSONA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Agent/rules/cm_persona.md'))

def load_persona():
    with open(PERSONA_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def generate_caption_prompt(topic, platform="Instagram"):
    """
    Constructs a prompt for the LLM to generate a caption.
    """
    import datetime
    persona = load_persona()
    date_str = datetime.datetime.now().strftime("%A %d %B %Y")
    
    prompt = f"""
    ROLE:
    {persona}

    TASK:
    Rédige un post pour {platform} sur le sujet suivant : "{topic}".
    
    CONTEXTE:
    Nous sommes aujourd'hui le {date_str}. Utilise la "Base de Connaissances (Planning)" du ROLE pour déduire l'emplacement si le sujet parle de "Demain", "Ce midi", "Ce soir", ou d'un jour précis.

    CONSIGNES:
    - Utilise le ton défini dans le ROLE.
    - Ajoute des emojis pertinents.
    - Ajoute 5 à 10 hashtags pertinents à la fin.
    - Sois concis et engageant.
    """
    return prompt

def generate_caption(topic, platform="Instagram"):
    """
    Simulates caption generation. In a real deployment, this would call OpenAI/Gemini API.
    """
    prompt = generate_caption_prompt(topic, platform)
    
    print("-" * 30)
    print("PROMPT SUGGÉRÉ POUR L'IA (Copier/Coller dans ChatGPT/Gemini) :")
    print("-" * 30)
    print(prompt)
    print("-" * 30)
    
    # Placeholder return
    return f"[Ceci est une simulation. Utilisez le prompt ci-dessus pour générer le texte réel.]\n\nSujet: {topic}"

if __name__ == "__main__":
    generate_caption("Menu du jour : Rougail Saucisse")
