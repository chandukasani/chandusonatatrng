from employee import Employee
from address import Address


address1=Address('hyderabad',567890)
address2=Address('relangi',534225)
emp1=Employee('chandu','kasani',address1)
emp2=Employee('chandu','kasani',[address1,address2])
print(emp1.getinitials())
print(emp1.Getfullname())
print(emp2.Getfullname())




