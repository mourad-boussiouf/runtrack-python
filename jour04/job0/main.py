import time
next_factor=2
operationString="1"

def factorialRecursion(user_input,operationString,next_factor):
    time.sleep(0.3)
    userInt=int(user_input)
    operationString+="*"+str(next_factor)
    print("operationString",operationString)
    if userInt==0:
        print("La factorielle de 0 est 1")
        return
    elif userInt==next_factor or userInt==1:
        print("La factorielle de "+user_input+" est ",eval(operationString))
        return
    elif userInt>next_factor:
        next_factor=next_factor+1
        print("recurs launch")
        print("userInt",userInt)
        print("operationString",operationString)
        print("next_factor",next_factor)
        factorialRecursion(user_input,operationString,next_factor)


user_input = input("Entrez un entier dont vous voulez la factorielle")
factorialRecursion(user_input,operationString,next_factor)