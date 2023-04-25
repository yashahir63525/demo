#13. Program to find smallest number of three numbers(if..elif..else)
no1=int(input("Enter First Number : "))
no2=int(input("Enter Second Number : "))
no3=int(input("Enter Third Number : "))
if(no1<no2 and no1<no3):
    print("no1 is Smallest")
elif(no2<no1 and no2<no3):
    print("no2 is Smallest")
else:
    print("no3 is Smallest")
