#3. Convert time inputted in minutes into hours and remaining minutes.

min=(int(input("Enter Minutes : ")))
hour=int(min/60)
r_m=int(min-(60*hour))
print ("H:M =",hour,":",r_m)
