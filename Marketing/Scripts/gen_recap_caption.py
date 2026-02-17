
import os
import sys

# Proposer une légende personnalisée
caption = (
    "Oté la famille ! 👋 Le soleil de la Réunion s'installe dans le 91 cette semaine ! ☀️🌋\n\n"
    "Voici notre planning pour ne pas nous rater :\n"
    "📍 Mardi Soir : Yerres, Av. de la Grange\n"
    "📍 Mercredi Midi : Yerres, Parvis du CEC\n"
    "📍 Mercredi Soir : Brunoy, Parvis de la Gare\n"
    "📍 Jeudi Midi : Clinique de Longjumeau\n"
    "📍 Vendredi Midi : Hôpital Privé du Val d'Yerres\n\n"
    "Au menu de la semaine : Rougail Saucisse, Cari Poulet et notre fameux Rougail Morue ! 🍛🌶️\n"
    "Sans oublier nos samoussas, bouchons et bonbons piment pour l'apéro... et une touche sucrée avec le gâteau patate ou le flan coco. 🍰🥥\n\n"
    "Venez voyager avec nous ! 🚚💨\n\n"
    "#CouleursPei #Reunion #FoodTruck #Yerres #Brunoy #Longjumeau #RougailSaucisse #CuisineReunionnaise #RougailMorue #LaReunion"
)

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../SocialMedia/recap_caption.txt')), 'w', encoding='utf-8') as f:
    f.write(caption)

print("CAPTION_GENERATED")
