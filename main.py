import string


def cesar_cipher(text, key, cipher=True):
    alphabet = string.ascii_lowercase
    resultat = ""

    for caractere in text:
        if caractere in alphabet:
            position = alphabet.index(caractere)
            new_position = (position + key) % len(alphabet) if cipher else (position - key) % len(alphabet)  # ou % 26
            new_caracter = alphabet[new_position]
            resultat += new_caracter      # --> ici on ajoute le resultats a la chaine de cractère deja existante
        else:
            resultat += caractere
    
    return resultat



def brute_force(text):
    for key in range(1, 26):
        decrypted_text = cesar_cipher(text, key) # --> appel de la fonction dechiffrement
        print(f"Décalage {key}: {decrypted_text}") # --> f-string = pour ajouter variable dans du text



print(cesar_cipher("nique zeubi", 6))  
print(cesar_cipher("erqmrxu oh prqgh", 3, cipher=False))
brute_force("erqmrxu oh prqgh") 




def cesar_cipher_two(text, key, cipher=True):
    resultat = ""

    for char in text:
            position = alphabet.index(caractere)
            new_position = (position + key) % len(alphabet) if cipher else (position - key) % len(alphabet)  # ou % 52
            new_caracter = alphabet[new_position]
            resultat += new_caracter      # --> ici on ajoute le resultats a la chaine de cractère deja existante
        else:
            resultat += caractere
    
    return resultat


def brute_force_two(crypted_text):
    for key in range(1, 1_114_112):
        decrypted_text = cesar_cipher_two(crypted_text, key, cipher=False) # --> appel de la fonction dechiffrement
        print(f"Décalage {key}: {decrypted_text}") 