#Find if a number is even or odd
y=int(input("Type in a number: "))
if y==0:
    print("It cannot be classified")
elif y%2==0:
    print("It is a even number")
else:
    print("It is an odd number")