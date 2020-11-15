class Guest:

    def __init__(self, name, age, wallet):
       self.name = name
       self.age = age
       self.wallet = wallet
       
    def charge_guest(self, money_out):
        self.wallet -= money_out
     

 

