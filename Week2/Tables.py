#print the multiplication table
x=int(input("give us a number: "))
for i in range(1,11):
    t=x*i
    print(f"{x}*{i} = {t}")
print("*"*30)