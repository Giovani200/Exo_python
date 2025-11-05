def run():
    # I Créer et typer correctement les variables suivantes 
    nom_boutique: str = "ChossettZ"
    produit: str = "chaussettes"
    prix_unitaire: float = 5.99
    quantite_stock: int = 20
    tva: float = 0.20
    compte_client: int = 100
    compte_boutique: int = 0

    #  II  phrase complète avec tous les variables

    print (f"Bienvenue chez {nom_boutique}! Nous vendons des {produit} au prix unitaire de {prix_unitaire} euros. Actuellement, nous avons {quantite_stock} unités en stock. La TVA applicable est de {tva}%. Votre compte client contient {compte_client} euros, et le compte de la boutique est à {compte_boutique} euros.")

    # III opérations arithmétiques suivantes
        # a prix hors taxe

    prix_ht = prix_unitaire
    print (f"Le prix hors taxe est de {prix_ht} euros.")

        # b prix toutes taxes comprises
    prix_ttc = prix_unitaire * (1 + tva)
    print (f"Le prix toutes taxes comprises est de {prix_ttc} euros.")

        # c  arrondis à 2 décimales des résultats précédents
    print (f"Le prix hors taxe  {prix_ht:.2f} euros.")
    print (f"Le prix toutes taxes  {prix_ttc:.2f} euros.")

    #  IV combien de paires de chaussettes il veut acheter

    nb_achat = input(f"Combien de paires de {produit} souhaitez-vous acheter ? ")

    # V Convertiion, vérification et si la quantité en stock est suffisante 

    try:
        quantite_achat = int(nb_achat)

        if quantite_achat <= 0:
            print("Erreur : La quantité doit être un nombre positif.")
            exit()

        if quantite_achat > quantite_stock:
            print(f"Erreur : Nous n'avons que {quantite_stock} unités en stock.")
            exit()

    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
        exit()

    # VI Calculer et stocker
    montant_ht_achat = prix_unitaire * quantite_achat
    montant_ttc_achat = prix_ttc * quantite_achat
    stock_restant = quantite_stock - quantite_achat
    compte_client = compte_client - montant_ttc_achat
    compte_boutique = compte_boutique + montant_ttc_achat

    # Afficher un récapitulatif clair
    print("\n" + "="*50)
    print("RÉCAPITULATIF DE LA VENTE")
    print("="*50)
    print(f"Produit : {produit}")
    print(f"Quantité achetée : {quantite_achat}")
    print(f"Montant HT : {montant_ht_achat:.2f}€")
    print(f"Montant TTC : {montant_ttc_achat:.2f}€")
    print(f"Stock restant : {stock_restant}")
    print(f"Votre compte client : {compte_client:.2f}€")
    print(f"Compte boutique : {compte_boutique:.2f}€")
    print("="*50 + "\n")


    # VII. Vérifier si le stock est inférieur à 10
    if stock_restant < 10:
        print("Alerte : Le stock est inférieur à 10 unités. Veuillez envisager de réapprovisionner.")

    # VIII. Condition supplémentaire
    if stock_restant < 15 and stock_restant > 10 and prix_unitaire > 5:
        print("!! Attention produit presque en rupture !!\n")


    # IX. Convertir le prix TTC de la vente en chaîne avec symbole €
    prix_ttc_vente_str = str(round(montant_ttc_achat, 2)) + "€"
    print(f"Montant total à payer (en chaîne) : {prix_ttc_vente_str}")


    # X. Afficher la facture formatée
    montant_tva = montant_ttc_achat - montant_ht_achat

    print("\n" + "-"*84)
    print(f"{nom_boutique:^84}")
    print("-"*84)
    print(f"Produit                           qté        HT")
    print(f"{produit.capitalize():<30} {'…'*20} {quantite_achat:>3} {montant_ht_achat:>10.2f}")
    print()
    print(f"                                                      Total HT : {montant_ht_achat:>10.2f}")
    print(f"                                                           TVA : {montant_tva:>10.2f}")
    print(f"                                                     Total TTC : {montant_ttc_achat:>10.2f}")


    # XI. Afficher le type de chaque variable à la fin du programme
    print("\n" + "="*84)
    print("TYPES DES VARIABLES")
    print("="*84)
    print(f"Type de nom_boutique : {type(nom_boutique)}")
    print(f"Type de produit : {type(produit)}")
    print(f"Type de prix_unitaire : {type(prix_unitaire)}")
    print(f"Type de quantite_stock : {type(quantite_stock)}")
    print(f"Type de tva : {type(tva)}")
    print(f"Type de compte_client : {type(compte_client)}")
    print(f"Type de compte_boutique : {type(compte_boutique)}")
    print(f"Type de prix_ht : {type(prix_ht)}")
    print(f"Type de prix_ttc : {type(prix_ttc)}")
    print(f"Type de nb_achat : {type(nb_achat)}")
    print(f"Type de quantite_achat : {type(quantite_achat)}")
    print(f"Type de montant_ht_achat : {type(montant_ht_achat)}")
    print(f"Type de montant_ttc_achat : {type(montant_ttc_achat)}")
    print(f"Type de stock_restant : {type(stock_restant)}")
    print(f"Type de montant_tva : {type(montant_tva)}")
    print(f"Type de prix_ttc_vente_str : {type(prix_ttc_vente_str)}")
    print("="*84)