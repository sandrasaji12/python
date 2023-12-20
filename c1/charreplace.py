a=str(input("Enter a string: "))
firstchar=a[0]
a=a.replace(firstchar,'$')
a=firstchar+a[1:]
print(a)
