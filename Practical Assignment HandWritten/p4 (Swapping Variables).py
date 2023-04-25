#4. write a program to swap two variables with and without temporary variables.

no1=10
no2=20
print("Before Swapping")
print("no1",no1)
print("no2",no2)

#with third variable
print ()
print("After Swapping with third Variable")
temp=no1
no1=no2
no2=temp
print("no1 =",no1)
print("no2 =",no2)

#without third variable
print()
print("After Swapping without third variable")
no1=10
no2=20
no1, no2=no2,no1
print("no1 =",no1)
print("no2 =",no2)
