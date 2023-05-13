next_factor=2
operationString="1"

def factorialRecursion(user_input,operationString,next_factor):
    userInt=int(user_input)
    operationString+="*"+str(next_factor)
    print("operationString",operationString)
    if userInt==0:
        print("La factorielle de 0 est 1")
        return
    elif userInt==next_factor or userInt==1:
        print("La factorielle de "+user_input+" est ",eval(operationString))
        integer2 = int('6')
        integer1 = int('3')
        print(int(integer2*integer1))
        return
    elif userInt>next_factor:
        next_factor=next_factor+1
        factorialRecursion(user_input,operationString,next_factor)


user_input = input("Entrez un entier dont vous voulez la factorielle")
factorialRecursion(user_input,operationString,next_factor)