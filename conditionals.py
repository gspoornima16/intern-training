# Number classifier(+ve/-ve/0)
x=int(input("Give me a number: "))
if x==0:
    print("The number is zero")
elif x > 0:
    print("It is a positive number")
else:
    print("It is a negative number")

#Find if a number is even or odd
y=int(input("Type in a number: "))
if y==0:
    print("It cannot be classified")
elif y%2==0:
    print("It is a even number")
else:
    print("It is an odd number")

#Grade calculator
z=int(input("Give me the mark you scored: "))
if z>100:
    print("It exceeds the highest score")
elif z>=90:
    print("Grade A")
elif z>=70:
    print("Grade B")
elif z>=50:
    print("Grade C")
elif z>=35:
    print("Grade D")
else:
    print("Grade F")

#password check
y="ABCD@1234"
password=input("Enter the password ")
if password==y:
    print("The password is correct")
else:
    print("The password you typed in is wrong")

#To find the largest of three numbers
x=int(input("No-1 "))
y=int(input("No-2 "))
z=int(input("N0-3 "))
if x>y:
    if x>z:
        print(x)
    else:
        print(z)
else:
    if y>z:
        print(y)
    else:
        print(z)

