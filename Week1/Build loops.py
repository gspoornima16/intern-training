#print the multiplication table
x=int(input("give us a number: "))
for i in range(1,11):
    t=x*i
    print(f"{x}*{i} = {t}")
print("*"*30)

# sum of every number (1-100) with an acccumulator
sum=0
for i in range(0,101):
    sum+=i
print(f"The total of 100 numbers is {sum}")
print("-"*30)

# Fizzbuzz
for x in range(1,51):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)
print("-"*30)

# guessing game
x=13
y= int(input("Take a Guess"))
while y!=x:
    if y>x:
        print("Try lower")
    else:
        print("Try higher")
    y= int(input("Take another guess"))
print("You guessed it right")