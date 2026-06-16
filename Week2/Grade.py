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