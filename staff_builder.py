from staff.employees import Employee
from staff.developer import Developer

worker1 = Employee('Jodie', 'Gardiner', 1)
worker2 = Employee('Richard', 'Dalton', 25)
worker3 = Employee('Gandalf', 'The Grey', 4)
worker4 = Developer('Barry', 'Bigstuff', 5, 'Python')

print worker1.get_details()
print worker2.get_details()
print worker3.get_details()
print worker4.get_details()