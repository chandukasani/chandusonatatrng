from leave import Leave

class restrictedleave(Leave):
    def __init__(self,employeeid,name,leavebalance,dateofbirth):
        self.dob=dateofbirth
        super().__init__(employeeid,name,leavebalance)

    def ApplyLeave(self):
        return self.Employeeid,self.Name,self.LeaveBalance,self.dob


