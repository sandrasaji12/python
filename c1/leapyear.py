c=int(input("Enter the current year:"))
f=int(input("Enter the final year:"))
print("Leap years are:")
for i in range(c,f):
    if(i%4==0) and (i%100!=0) or (i%400==0):
        print(i)
