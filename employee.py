import random 

class EmployeeWage:
    def __init__(self) -> None:
        self.wage_per_hour = 20
        self.full_day = 8
        self.total_wage = 0
    
    def check_attendance(self):
        attendance = random.choice(["present", "absent"])
        return attendance
        
        
    def calculate_wage(self):
        emp_status = self.check_attendance()
        if emp_status == 'present':
            self.total_wage = self.wage_per_hour * self.full_day
            print("the Employee is present")
        else:
            print("The Employee is absent")
        
emp1= EmployeeWage()
emp1.calculate_wage()
print(emp1.total_wage)