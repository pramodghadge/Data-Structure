

raiseMap = dict(
    NY = 4,
    CA = 5,
)

class Employee(object):
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@mycompany.com"
        self.salary = salary

    #
    def __repr__(self):
        return "Employee('{0}', '{1}', {2})".format(self.first, self.last, self.salary)

class EmployeeNew(Employee):
    def __init__(self, first, last, salary, designation, location):
        self.location = location
        self.designation = designation
        super(EmployeeNew, self).__init__(first, last, salary)

    def get_raise(self):
        return raiseMap.get(self.location, 1.04)

    def __repr__(self):
        return "New Employer has following atr. First name:{0}, Last Name: {1}, " \
               "Salary:{2}, Designation:{3}, Location:{4}, raise for location:{5}".format(
            self.first,
            self.last,
            self.salary,
            self.designation,
            self.location,
            self.get_raise()
        )


if __name__ == '__main__':
    empA = Employee("Pramod", "Ghadge", "10000")
    print empA


    emp = EmployeeNew("Pramod", "Ghadge", "10000", "Software Engineer", "NY")
    print emp

    empB = EmployeeNew("Pramod", "Ghadge", "10000", "Software Engineer", "TX")
    print empB
