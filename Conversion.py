def conversion(durée,unité):
    h = 0
    m = 0
    s = 0
    # Conversion en secondes (unité la plus basse)
    if unité == "h":
        durée = durée*3600
    elif unité == "m":
        durée = durée*60
    elif unité == "s":
        pass
    else:
        print("Erreur d'unité")
    # incrémentation des heures, minutes, le restant étant les secondes
    while durée >= 3600:
        h += 1
        durée -= 3600

    while durée >= 60:
        m += 1
        durée -= 60

    s = int(durée)

    # Mise en forme/affichage du résultat final
    print("{} heures,{} minutes,{} secondes.".format(h,m,s))
