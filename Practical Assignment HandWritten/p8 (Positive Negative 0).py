#8. Program to check number is positive, negative or zero(nested if)

no=float(input("Enter a number to check Positive/Negative/0 : "))
if no>=0:
    if no == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")
    
