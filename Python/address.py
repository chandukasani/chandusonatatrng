class Address:
    def __init__(self,address):
        self.address=address

    def getaddress(self):
        return self.address

add=Address('relangi')
ad=add.getaddress()
print(ad)

