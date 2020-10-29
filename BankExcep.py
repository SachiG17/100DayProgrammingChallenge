class MinBalException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg

class NegativeAmountException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
    
Bal = 500
withdrawal_amount= int(input("Enter the amount to withdraw\n"))

try:
    if (withdrawal_amount > Bal):
        e=MinBalException("Amount greater than Balance")
        raise e
    elif (withdrawal_amount <= 0):
        e=NegativeAmountException("Enter proper amount")
        raise e
    else:
        Bal=(Bal-withdrawal_amount)
        print("Your remaining amount is ",Bal)

except MinBalException as e :
    print(e)
except NegativeAmountException as e:
    print(e)