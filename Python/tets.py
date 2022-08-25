class Student:
    def __init__(self,student_id,student_name):
        self.studentid=student_id
        self.studentname=student_name

    def test(self):
        return self.studentid,self.studentname

st=Student(21,'chandu')
s=st.test()
print(s)

