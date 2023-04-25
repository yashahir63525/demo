#12. Program to find largest number of three numbers(nested if)
no1=int(input("Enter First Number : "))
no2=int(input("Enter Second Number : "))
no3=int(input("Enter Third Number : "))
if(no1>no2):
    if(no1>no3):
        print("no1 is Largest")
if(no2>no1):
    if(no2>no3):
        print("no2 is Largest")
else:
    print("no3 is Largest")
