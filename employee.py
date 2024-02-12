import random 

class Employee_Wage():
    def check_attendance(self):
        self.attendance= random.choice(["present", "absent"])
        if (self.attendance=='present'):
            print("the Employee is present")
        else:
            print("The Employee is absent")

emp1= Employee_Wage()
emp1.check_attendance()
