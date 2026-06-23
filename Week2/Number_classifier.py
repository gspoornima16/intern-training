# Number classifier(+ve/-ve/0)
x=input("Give me a number: ")
try:
    if x==0:
        print("The number is zero")
    elif x > 0:
        print("It is a positive number")
    else:
        print("It is a negative number")
except Exception:
    print("Type in an integer")