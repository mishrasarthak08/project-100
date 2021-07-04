class atm(object):
    def __init__(self,cn,pn):
        self.cardnumber:cn
        self.pinnumber:pn

    def Cash(self):
            print("Cash is withdrawling!")

    def Balance(self):
            print("your balance is 50000 ")


def display():
    atmd = atm("23434344343","354534545344")
    print(atmd)
    atmd.Cash()
    atmd.Balance()
        
display()   