# -*- coding: utf-8 -*-

from app.front import *
from app.init import *

def jouer_tour(scores):
    menu()
    
    while True:
        choix = input("→ ").strip().lower()
        
        if choix not in ['1', '2', '3', 'q']:
            message_erreur()
            continue
        
        if choix == 'q':
            return False
        
        break
    
    mon_choix = convertir(choix)
    choix_pc = ordi()

    montrer_choix(mon_choix, choix_pc, icones)
    
    res = gagnant(mon_choix, choix_pc)
    resultat_manche(res)
    
    maj_scores(scores, res)
    afficher_scores(scores)
    
    return True

def main():
    scores = {'joueur': 0, 'ordi': 0, 'nul': 0}
    
    title()
    
    continuer = True
    while continuer:
        continuer = jouer_tour(scores)
        if continuer:
            input("\n[Entrée pour continuer...]")
    
    fin_partie(scores)

if __name__ == "__main__":
    main()