alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def function(arg):
    for char in arg:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower()) + 1
            print(char.lower(), "Est dans l'alphabet à la position: ", index)
        else:
            print(char.lower(), "Votre string contient un caractère qui n'est pas dans l'aphabet, le script va s'arrêter.")
            return

user_input = input("Entez votre input: ")
function(user_input)