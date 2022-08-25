class Student:
    def __init__(self,student_id,student_name,__studentdept):
        self.stdid=student_id
        self.stdname=student_name
        self.__stddept=__studentdept

    def studentdetails(self):
        return self.stdid,self.stdname,self.__stddept

std=Student(2345,'chandu',345)
sd=std.studentdetails()
print(sd)

setattr(std,'student_class',10)
print(getattr(std,'student_class'))
print(hasattr(std,'student_class'))

delattr(std,'student_class')
print(hasattr(std,'student_class'))

setattr(std,'student_class',12)
print(getattr(std,'student_class'))
print(hasattr(std,'student_class'))

print(sd)
print(getattr(std,'student_class'))





