alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def function(arg):
    Newarg=''
    for char in arg:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower()) + 1
            Newarg=Newarg+alphabet[index-1]
            print(char.lower(), "Est dans l'alphabet à la position: ", index,alphabet[index-1])
        else:
            print(char.lower(), "Votre mot contient un caractère qui n'est pas dans l'aphabet, le script va s'arrêter.")
            return
    print(Newarg)

user_input = input("Entez votre input: ")
function(user_input)