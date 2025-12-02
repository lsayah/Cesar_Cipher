import string





def chiffrement(texte, decalage):
    alphabet = string.ascii_lowercase
    resultat = ""

    for caractere in texte:
        if caractere in alphabet:
            position = alphabet.index(caractere)
            nouvelle_position = (position + decalage) % len(alphabet)  # ou % 26
            nouveau_caractere = alphabet[nouvelle_position]
            resultat += nouveau_caractere      # --> ici on ajoute le resultats a la chaine de cractère deja existante
        else:
            resultat += caractere
    
    return resultat



def dechiffrement(texte,decalage):
    alphabet = string.ascii_lowercase
    resultat = ""

    for caractere in texte:
        if caractere in alphabet:
            position = alphabet.index(caractere)
            nouvelle_position = (position - decalage) % len(alphabet)  # ou % 26
            nouveau_caractere = alphabet[nouvelle_position]
            resultat += nouveau_caractere  # --> ici on ajoute le resultats a la chaine de cractère deja existante
        else:
            resultat += caractere # --> pour gerer le non caractère

    return resultat


def brute_force(texte):
    for decalage in range(1, 26):
        texte_dechiffre = dechiffrement(texte, decalage) # --> appel de la fonction dechiffrement
        print(f"Décalage {decalage}: {texte_dechiffre}") # --> f-string = pour ajouter variable dans du texte



print(chiffrement("bonjour le monde", 3))  # Exemple d'utilisation
print(dechiffrement("erqmrxu oh prqgh", 3))
brute_force("erqmrxu oh prqgh")  # Exemple d'utilisation