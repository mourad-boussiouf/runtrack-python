def readTextFile(string):
    extension = ".txt"
    fileName = "../%s%s"%(string, extension)
    f = open(fileName, "r")
    print(f.read())
user_input = input("Entrez le nom du fichier text que vous voulez lire(output par defaut)")
readTextFile(user_input)