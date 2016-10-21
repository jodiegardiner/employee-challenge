class Employee:
    #BASE_SALARY = 5000
    employee_number = 0

    def __init__(self, fname, sname, noofyears, base_salary=5000 ):
        Employee.employee_number += 1
        self.sname = sname
        self.fname = fname
        self.noofyears = noofyears
        self.employee_number = Employee.employee_number
        self.base_salary = base_salary


    ''' calculate the base salary plus
    any bonus based on numer of years worked '''

    def calculate_salary(self):
        bonus = 0
        base_salary = self.base_salary
        if self.noofyears < 3:
            bonus = base_salary * 0.01
        elif self.noofyears <= 5:
            bonus = base_salary * 0.05
        elif self.noofyears > 5:
            bonus = base_salary * 0.25
        return base_salary + bonus

    def get_details(self):
        return ' \n------------------------\n First Name: %s\n Surname %s\n Years Worked: %s\n Employee Number: %s\n Salary: %s' \
               % (self.fname, self.sname, self.noofyears, self.employee_number, self.calculate_salary())