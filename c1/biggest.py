a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if(a>=b and a>=c):
    print(a,"is the biggest")
elif(b>=a and b>=c):
    print(b,"is the biggest")
else:
    print(c,"is the biggest")