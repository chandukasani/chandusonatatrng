class Leave:
    def __init__(self,employeeid,name,leavebalance):
        self.employeeid=employeeid
        self.name=name
        self.leavebalance=leavebalance

    def applyleave(self):
        return self.employeeid,self.name,self.leavebalance






