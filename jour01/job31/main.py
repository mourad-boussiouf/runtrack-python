alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def function(arg):
    Newarg=''
    NewMot=''
    count = 0
    for char in arg:
        if char.lower() in alphabet:
            count=count+1
            index = alphabet.index(char.lower()) + 1
            if count == len(arg):
                NewMot = Newarg+alphabet[index]
            Newarg=Newarg+alphabet[index-1]
            print(char.lower(), "Est dans l'alphabet à la position: ", index,alphabet[index-1],count)
        else:
            print(char.lower(), "Votre mot contient un caractère qui n'est pas dans l'alphabet, le script va s'arrêter.")
            return
    print(Newarg, "plus loin dans l'alphabet donne", NewMot)

user_input = input("Entez votre input: ")
function(user_input)