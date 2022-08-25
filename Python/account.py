class Account:
    def __init__(self,acno,name,type,balance):
        self.acno=acno
        self.name=name
        self.type=type
        self.balance=balance

    def details(self):
        return self.acno,self.name,self.type,self.balance


