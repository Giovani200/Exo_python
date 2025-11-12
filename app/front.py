import time

rouge = '\033[91m'
vert = '\033[92m'
jaune = '\033[93m'
cyan = '\033[96m'
reset = '\033[0m'


def lettre(txt):
    for lettre in txt:
        print(lettre, end='', flush=True)
        time.sleep(0.04)
    print()

def title():
    print(f"\n{cyan}✊✋✌ Pierre Papier Ciseaux ✊✋✌{reset}\n")


def menu():
    print(f"{jaune}Choisis:{reset}")
    print("1 → 🪨 Pierre")
    print("2 → 📄 Papier") 
    print("3 → ✂️ Ciseaux")
    print("q → Quitter\n")


def afficher_scores(scores):
    print(f"\n{cyan}SCORES:{reset} Toi: {vert}{scores['joueur']}{reset} | Ordi: {rouge}{scores['ordi']}{reset} | Nul: {scores['nul']}\n")

def montrer_choix(choix_j, choix_o, icones):
    print(f"\nTu joues: {icones[choix_j]} {choix_j}")
    time.sleep(0.3)
    print(f"Ordi joue: {icones[choix_o]} {choix_o}")

def resultat_manche(res):
    if res == "gagné!":
        lettre(f"{vert}🎉 Tu gagnes!{reset}")
    elif res == "L'ordinateur gagne!":
        lettre(f"{rouge}L'ordi gagne{reset}")
    else:
        lettre(f"{jaune}Égalité!{reset}")

def message_erreur():
    print(f"{rouge}⚠ Entre 1, 2, 3 ou q!{reset}\n")

def fin_partie(scores):
    print(f"\n{cyan}Fin du jeu!{reset}")
    afficher_scores(scores)