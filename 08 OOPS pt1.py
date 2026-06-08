#1 Create a student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class student:
    def __init__ (self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        sum = self.m1 + self.m2 + self.m3
        av = sum/3
        print("Hii", s1.name,"Your average is:",av)

s1=student("Aman",98,85,91)
s1.avg()

#2 Create account class with 2 attributes- balance & account number. Then create method for debit, credit & printing the balance.
class account:
    def __init__ (self, balance, accountnumber):
        self.balance = balance
        self.accountnumber = accountnumber

    
    
    def deb(self):
        debit = int(input("How much money you want to debit:"))
        self.balance -= debit
        print("Ruppes", debit , "was debited")
        print("Total balance in account is:", self.balance)
    
    def cre(self):
        credit = int(input("How munch money you want to credit"))
        self.balance += credit
        print("Ruppes", credit , "was credited")
        print("Total balance in account is:", self.balance)

    def prt_bal(self):
        return self.balance

acc1 = account(5000,2154653134854)
acc1.deb()
acc1.cre()
acc1.prt_bal()