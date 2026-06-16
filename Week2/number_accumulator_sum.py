#sum of n numbers
n=int(input("Give me a number to sum from 0 to n:"))
sum=0
for i in range(0,n+1):
    sum+=i
print(f"The sum of 0 to {n} number is {sum}")
print("-"*30)