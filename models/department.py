class Department:
    def __init__(self,department):
        self.department = department
        self.employers = []

    def displayDepartment(self):
        print('Department: ' + self.department)

    def displayEmployers(self):
        for i in self.employers:
            print(i.displayFullName())

    def addEmployer(self, employer):
        '''Add an Employer object'''
        self.employers.append(employer)

    def removeEmployer(self, employer):
        '''remove an Employer object'''
        self.employers.remove(employer)