import random

icones = {
    "papier": "📄",
    "ciseaux": "✂️",
    "pierre": "🪨",
}

tuples = [
    ("ciseaux", "papier"),
    ("pierre", "ciseaux"),
    ("papier", "pierre"),
]

def ordi():
    return random.choice(["pierre", "papier", "ciseaux"])

def convertir(entree):
    coups = ['pierre', 'papier', 'ciseaux']
    return coups[int(entree) - 1]

def gagnant(joueur, ordi):
    if joueur == ordi:
        return "Égalité!"
    
    for vainqueur, perdant in tuples:
        if joueur == vainqueur and ordi == perdant:
            return "gagné!"
        
    return "L'ordinateur gagne!"

def maj_scores(scores, resultat):
    if resultat == "gagné!":
        scores['joueur'] += 1 
    elif resultat == "L'ordinateur gagne!":
        scores['ordi'] += 1
    elif resultat == "Égalité!":
        scores['nul'] += 1
    else:
        pass
