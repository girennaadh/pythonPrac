class bank:
     def __init__(self,a):
         self.b=a

     def kyc(self,fname,lname):
        firstname=fname
        lastname=lname
        print firstname
        return
     def deposit(self,money):
        self.deposit=money
        print money
        return

     def totalmoney(self):    
        money=10
        totalmoney=self.deposit+money
        print totalmoney
        return

p1=bank("k")
p1.kyc("giri","nath")
p1.deposit(1000)
p1.totalmoney()
