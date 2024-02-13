import random 

class EmployeeWage:
    # def __init__(cls):
    full_day = 8
    wage_per_hour = 20
    total_wage = 0
    part_time_hr = 4
    max_work_days=25
    max_work_hours =100
    hours_worked = 0
    days_worked=0
    
    @classmethod
    def check_attendance(cls):
        attendance = random.choice(["present", "absent","half_day"])
        return attendance
        
    @classmethod
    def calculate_wage(cls):
        emp_status = cls.check_attendance()
        match emp_status:
            
            case 'present':
                    cls.total_wage += cls.wage_per_hour * cls.full_day
                    cls.hours_worked += cls.full_day
                    # cls.total_month_wage=cls.wage_per_hour*cls.full_day*cls.total_work_days
                    print("the Employee is present on full day working")
            case "half_day":
                cls.total_wage += cls.wage_per_hour * cls.part_time_hr
                cls.hours_worked += cls.part_time_hr
                print("the Employee is on Half day working")
                
            case _:
                print("The Employee is absent")
    @classmethod       
    def monthly_wage(cls):
        while cls.hours_worked < cls.max_work_hours and cls.days_worked < cls.max_work_days:
            cls.days_worked += 1
            cls.calculate_wage()


emp1= EmployeeWage()
emp1.monthly_wage()
print(emp1.total_wage, emp1.hours_worked, emp1.days_worked)
