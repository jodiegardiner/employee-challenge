from staff.employees import Employee

worker1 = Employee('Jodie', 'Gardiner', '1', 1)
worker2 = Employee('Richard', 'Dalton', '2', 25)
worker3 = Employee('Gandalf', 'The Grey', '3', 4)


def calculate_salary(staff):
    salary = staff._base_salary
    if staff._noofyears < 4:
        salary = staff._base_salary *1.01
    elif staff._noofyears == (4 or 5):
        salary = staff._base_salary * 1.05
    elif staff._noofyears > 5:
        salary = staff._base_salary * 1.25
    return salary

print calculate_salary(worker1)
print calculate_salary(worker2)
print calculate_salary(worker3)