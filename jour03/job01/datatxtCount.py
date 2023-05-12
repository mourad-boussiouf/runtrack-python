def readTextFile(string):
    if string=='':
        string = 'data'
    extension = ".txt"
    fileName = "../%s%s"%(string, extension)
    f = open(fileName, "r")
    Datastring = f.read()
    print(len(Datastring.split()))
user_input = input("Entrez le nom du fichier dont vous voulez le nombre de mot, laissez vide si le fichier est data.txt")
readTextFile(user_input)