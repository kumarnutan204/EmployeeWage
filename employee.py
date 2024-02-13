import random 

class EmployeeWage:
    def __init__(self, name,full_day,wage_per_hour,max_work_days,max_work_hours, emp_type):
        self.emp_name = name
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


class Company:
    
    def __init__(self, name):
        self.company_name = name
        self.employee_dict = {}
        
        
    def add_employee(self, emp_obj):
        self.employee_dict.update({emp_obj.emp_name: emp_obj})
        print("Employee name added to the company dictionary")
        
    def get_employee(self, emp_name):
        return self.employee_dict.get(emp_name)
        
    def display_employee(self):
        return(self.employee_dict)
    def delete_employee(self, emp_name):
        del self.employee_dict[emp_name]
        return self.employee_dict
        
        """
        display, update, delete
        """
        
def add():
    emp_name=input("Enter the employee name: ")
    if emp_name not in company.employee_dict.keys():
        print(company.display_employee())
        f_d_w=int(input("Enter 8 the full day work hours :")) #f_d_w= full day work hours
        w_p_h= int(input("Enter 20 the wage per hour for your company: "))#w_p_h=wage per hour
        max_w_h= int(input("Enter 100 the max working hours for your company: "))#max_w_h = max working hours
        max_w_d= int(input("Enter 25 the max working days for your company: "))#max_w_d= max working days 

        status= input("Enter 'half_day' a part time employee else enter full day: ")

        emp= EmployeeWage(emp_name, f_d_w,w_p_h,max_w_d,max_w_h,status)
        emp.monthly_wage()
        print(emp.total_wage, emp.hours_worked, emp.days_worked)
        company.add_employee(emp)
        # company.get_employee(emp_name)
        print(company.display_employee())
    else:
        print('Employee already exists')
        # choice= int(input("Enter 1 to show all employees"))
        # if choice==1:
        #     company.display_employee()


if __name__ == '__main__':
    company_name = input("Enter the company name ")
    company = Company(company_name)
    add()
    company.display_employee()
    
    
    
