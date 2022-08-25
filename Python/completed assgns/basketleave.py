from leave import Leave

class basketofleave(Leave):
    def __init__(self,employeeid,name,leavebalance,reasonforapplyingleave):
        self.rfal=ReasonForApplyingLeave
        super().__init__(employeeid,name,leavebalance)

    def applyleave(self):
        return self.employeeid,self.name,self.leavebalance,self.rfal




