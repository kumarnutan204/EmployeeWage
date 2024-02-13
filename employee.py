import random 

class EmployeeWage:
    def __init__(self,full_day,wage_per_hour,max_work_days,max_work_hours, emp_type):
        self.full_day = full_day
        self.wage_per_hour = wage_per_hour
        self.total_wage = 0
        self.part_time_hr = 4
        self.max_work_days= max_work_days
        self.max_work_hours = max_work_hours
        self.hours_worked = 0
        self.days_worked=0
        self.emp_type=emp_type
        
    
    
    def check_attendance(self):
        if self.emp_type!="half_day":
            attendance = random.choice(["present", "absent"])
            return attendance
        else: 
            attendance = random.choice(["absent","half_day"])
            return attendance
    
    def calculate_wage(self):
        emp_status = self.check_attendance()
        if emp_status== 'present':
                self.total_wage += self.wage_per_hour * self.full_day
                self.hours_worked += self.full_day
                # self.total_month_wage=self.wage_per_hour*self.full_day*self.total_work_days
                print("the Employee is present on full day working")
        if emp_status== "half_day":
            self.total_wage += self.wage_per_hour * self.part_time_hr
            self.hours_worked += self.part_time_hr
            print("the Employee is on Half day working")
            
        else:
            print("The Employee is absent")
      
    def monthly_wage(self):
        while int(self.hours_worked) < int(self.max_work_hours) and int(self.days_worked) < int(self.max_work_days):
            self.days_worked += 1
            self.calculate_wage()


f_d_w=int(input("Enter 8 the full day work hours "))
w_p_h= int(input("Enter 20 the wage per hour for your company"))
max_w_h= int(input("Enter 100 the max working hours for your company"))
max_w_d= int(input("Enter 25 the max working days for your company"))

status= input("Enter 'half_day' a part time employee else enter full day")

emp1= EmployeeWage(f_d_w,w_p_h,max_w_d,max_w_h,status)
emp1.monthly_wage()
print(emp1.total_wage, emp1.hours_worked, emp1.days_worked)
