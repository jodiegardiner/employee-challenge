from staff.employees import Employee

class Developer(Employee):
    def __init__(self, fname, sname, noofyears, lang='Python'):
        self.lang = lang
        Employee.__init__(self, fname, sname, noofyears)

    def calculate_salary(self):
        salary = Employee.calculate_salary(self)
        if self.lang == 'Python':
            salary = salary * 1.1
        return salary


    def get_details(self):
        return Employee.get_details(self) +'\n Language: %s' % self.lang