import random 

class EmployeeWage:
    def __init__(self):
        self.wage_per_hour = 20
        self.full_day = 8
        self.total_wage = 0
        self.part_time_hr = 4
        self.max_work_days=25
        self.max_work_hours =100
        self.hours_worked = 0
        self.days_worked=0
    
    def check_attendance(self):
        attendance = random.choice(["present", "absent","half_day"])
        return attendance
        
        
    def calculate_wage(self):
        emp_status = self.check_attendance()
        match emp_status:
            
            case 'present':
                    self.total_wage += self.wage_per_hour * self.full_day
                    self.hours_worked += self.full_day
                    # self.total_month_wage=self.wage_per_hour*self.full_day*self.total_work_days
                    print("the Employee is present on full day working")
            case "half_day":
                self.total_wage += self.wage_per_hour * self.part_time_hr
                self.hours_worked += self.part_time_hr
                print("the Employee is on Half day working")
                
            case _:
                print("The Employee is absent")
                
    def monthly_wage(self):
        while self.hours_worked < self.max_work_hours and self.days_worked < self.max_work_days:
            self.days_worked += 1
            self.calculate_wage()


emp1= EmployeeWage()
emp1.monthly_wage()
print(emp1.total_wage, emp1.hours_worked, emp1.days_worked)
