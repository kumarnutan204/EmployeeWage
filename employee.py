import random 

class EmployeeWage:
    def __init__(self):
        self.wage_per_hour = 20
        self.full_day = 8
        self.total_wage = 0
        self.part_time_hr = 4
    
    def check_attendance(self):
        attendance = random.choice(["present", "absent","half_day"])
        return attendance
        
        
    def calculate_wage(self):
        emp_status = self.check_attendance()
        if emp_status == 'present':
            self.total_wage = self.wage_per_hour * self.full_day
            print("the Employee is present")
        elif emp_status=="half_day":
            self.total_wage = self.wage_per_hour * self.part_time_hr
            print("the Employee is on Half day working")
            
        else:
            print("The Employee is absent")


emp_part1= EmployeeWage()
emp_part1.calculate_wage()
print(emp_part1.total_wage)