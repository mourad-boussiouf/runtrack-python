alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def function(arg):
    for char in arg:
        if char.lower() in alphabet:
            print(char.lower(), "dans l'array alphabet")
        else:
            print(char.lower(), "Votre input contient des caractères non alphabétiques ou spéciaux")
            return

user_input = input("Entez votre input: ")
function(user_input)