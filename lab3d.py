class employee258:
    empcount=0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        employee258.empcount+=1
    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)

    def displayCount(self):
        print("Total employee %d" , employee258.empcount)
e1=employee258("Ali",9000)
e2=employee258("omer",25800)
e3=employee258("Asad",2800)
e1.displayEmployee()
e2.displayEmployee()
e3.displayEmployee()
print("Total Employee " , employee258.empcount)
