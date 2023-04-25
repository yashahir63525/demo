#10. Program to check prime number
num=int(input("Enter a number : "))
flag = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True  # if factor is found, set flag to True
            break
if flag:  # check if flag is True
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
