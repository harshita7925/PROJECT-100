class Atm:
    def _init_(self,atm_card_number,pin_number):
        self.atm_card_number=atm_card_number
        self.pin_number=pin_number
    
    def cash_withdrawl(self,amount):
        current_amount=50000-amount
        print("I have withdrawn this:"+str(amount)+"My remaining balance is this:"+str(current_amount))
    
    def balance_enquiry(self):
        print("I have 10 lakhs rupees in my balance")
    
def main():
    atm_card_number=input("Enter your card number:")
    pin_number=input("Enter your pin number:")
    new_user=Atm(atm_card_number,pin_number)
    print("Choose your activity:")
    print("1.Balance Enquiry  2.Cash Withdrawl")
    activity=input("Enter the activity number:")
    if activity==1:
        new_user.balance_enquiry()
    
    elif activity==2:
        amount=input("Enter the amount that you want to withdraw:")
        new_user.cash_withdrawl(amount)
    
    else:
        print("Enter a valid pin number:")

if _name_=='_main_':
    main()