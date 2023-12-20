class Bank:
    def __init__(self, a, n, t, b):
        self.ac = a
        self.name = n
        self.type = t
        self.bal = b

    def depo(self, a1):
        self.bal += a1
        print("balance : ", self.bal)

    def withdraw(self, a2):
        if self.bal < a2:
            print("Insufficient balance...")
        else:
            self.bal -= a2
            print("Balance : ", self.bal)

    def display(self):
        print("Account No : ", self.ac)
        print("Name : ", self.name)
        print("Account Type : ", self.type)
        print("Account Balance : ", self.bal)


a = int(input("Enter acc no : "))
n = input("Enter name : ")
t = input("Enter acc type : ")
b = int(input("Enter balance : "))
obj1 = Bank(a, n, t, b)
obj1.display()
a1 = int(input("Enter the amount to deposit:"))
obj1.depo(a1)
a2 = int(input("Enter the amount to withdraw:"))
obj1.withdraw(a2)
