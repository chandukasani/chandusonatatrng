from address import Address
class Employee:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def getinitials(self):
        return self.firstname[0]+ ''+self.lastname[0]
    def getfullname(self):
        return self.firstname + ' ' +self.lastname



