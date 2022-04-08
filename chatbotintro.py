import nltk #importation de ntlk (Natural Language Toolkit)
from nltk.chat.util import Chat, reflections # Importation des packages nécessaires

# Importation d'un module de création et d'affichage de la date et de l'heure
import datetime
now = datetime.now() # Création d'une instance
current_time = now.strftime("%H:%M:%S") # Formatage de l'affichage et enregistrement dans une variable

# Définition du dialogue
pairs = [
    ["(Je m'appelle | Mon nom | Je me nomme) (.*)", ["Salut %1"]], # Création des pairs et utilisation des regex pour
    ["(bonjour|salut|coucou|salamalekoum)", ["Salut toi", 'que puis-je faire pour toi ?']],
    ["(.*)(ville|adresse)", ["Nous somme à Dakar"]]
    ["(.*)aider(.*)", ["Je peux vous aider"]]
    ["(.*)merci(.*)", ["De rien et à bientôt"]]
    ['content', ['Moi aussi, je suis content !']], ['triste', ["Cela ne peut que s'arranger!"]],
    ['ordinateur', ['Nous allons prendre le pouvoir !']], ['musique', ["Dip ou Wally ?"]],
    ['python', ['Un très bon language de programmation']],
    ["(.*)date(.*)", ["Aujourd'hui nous devrions être le ..."]],
    ["(.*)heure(.*)", ["Il doit-être environ "+current_time]],
    ["(.*)", ["Vraiment ?", "Tu en es certain ?", "Hmmmmm.", "Remarquable...", "Je ne suis pas certain d'acquiescer...", "Absolument !",
    "Faut voir !", "Que disions-nous au fait ?", "Ce qui veut dire quoi ?", "Tu as sans doute raison.", "N'importe quoi ! Mais où on va, là !",
    "Bref, tes projets pour demain ?", "Je me disais exactement la même chose.", "Bien des gens sont de cet avis.", "Plusieurs personnes m'ont dit cela déjà.",
    "Merveilleux !", "Cela pourrait s'avérer embarrassant !", "Tu es vraiment de cet avis ?", "Effectivement...", "C'est ce que je voulais dire !",
    "Eventuellement..."]]
    ]


chat = Chat(pairs, reflections)
chat.converse()
