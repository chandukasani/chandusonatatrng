class Employee:
    def __init__(self,fname,lname,address):
        self.firstname=fname
        self.lastname=lname
        self.address=address

    def Getfullname(self):
        return self.firstname,self.lastname ,self.address

    def getinitials(self):
        return self.firstname[0].upper()+self.lastname[0].upper()

