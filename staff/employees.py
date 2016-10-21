class Employee:
    base_salary = 5000
    employee_number = 0

    def __init__(self, fname, sname, noofyears):
        Employee.employee_number += 1
        self.fname = fname
        self.sname = sname
        self.employee_number = Employee.employee_number
        self.noofyears = noofyears

    def calculate_salary(self):
        salary = self.base_salary
        if self.noofyears < 4:
            salary = self.base_salary * 1.01
        elif self.noofyears == (4 or 5):
            salary = self.base_salary * 1.05
        elif self.noofyears > 5:
            salary = self.base_salary * 1.25
        return salary

    def get_details(self):
        return ' \n------------------------\n First Name: %s\n Surname %s\n Years Worked: %s\n Employee Number: %s\n Salary: %s' \
               % (self.fname, self.sname, self.noofyears, self.employee_number, self.calculate_salary())

