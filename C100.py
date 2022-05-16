class Atm(object):
    def check_balance(self):
        print("Your balance is 50000")
    def withdrawal(self,amount):
        new_amount=50000-amount
    print("you have withdrawn amount"+str(amount)+".Your remaining balance is"+str(new_amount))