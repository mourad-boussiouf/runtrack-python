def createTextFile(string):
    f=open("../output.txt", "w")
    f.write(string)
    print("Fichier crée.")

user_input = input("Entrez le text à mettre dans le fichier: ")
createTextFile(user_input)