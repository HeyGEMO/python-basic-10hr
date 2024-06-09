class account:
    def __init__(self,balance,acc_no) -> None:
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance:",self.print_bal())
        
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("total balance:",self.print_bal())

    def print_bal(self):
        return self.balance
acc1=account(10000,1234)
print(acc1.balance)
print(acc1.acc_no)
acc1.debit(1000)
acc1.credit(900)
acc1.print_bal()