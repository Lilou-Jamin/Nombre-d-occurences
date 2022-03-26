file = open ('texte.txt', 'r', encoding='utf-8') # Appel du fichier utilisé
fichier = open("nboccurrence.html", "w") # On ouvre le document html du site pour pouvoir le modifier
fichier.write("<h1> Le nombre d'occurrence dans ce texte est de :<h1>") # Titre dans le site web
listUnique = [] # On crée une liste unique pour pouvoir mettre les mots qui n'apparaissent qu'une seule fois
#dedans et ne pas répété les mots qui apparaissent à plusieurs reprises

content = file.read() # On lit le contenu du fichier texte
listMots = content.split() # On met le contenu du texte splité dans une liste qui est l'occurrence ListMots
file.close() # On ferme le fichier là où le texte se trouve, nous n'en n'avons plus besoin

fichier.write("""<table border="1" cellpadding="15"> <!--Création du tableau-->
       <tr>
          <th>Mot</th>                  <!-- Titre des catégories-->
          <th>Nombre occurence</th>     <!-- Titre des catégories-->
       </tr>""")

for mot in listMots :
    if mot not in listUnique:
        listUnique.append(mot) # Si un mot n'est pas dans la liste unique on l'ajoute
        fichier.write("""<tr>
        <td>"""+mot+"""</td> <!-- On affiche le mot compté dans le tableau -->
        <td>"""+str(listMots.count(mot))+"""</td></tr>""") # Nombre d'occurrences du mot

fichier.close()# On ferme le fichier html




