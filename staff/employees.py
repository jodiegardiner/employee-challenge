class Employee:
    def __init__(self, fname, sname, id, noofyears, base_salary=50000):
        self._base_salary = base_salary
        self._fname = fname
        self._sname = sname
        self._id = id
        self._noofyears = noofyears