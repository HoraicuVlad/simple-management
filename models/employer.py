class Employer:
    def __init__(self,first_name,last_name,age,job,salary,bonus):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total_salary = salary
    
    def __str__(self):
        return ' First name: ' + self.first_name + ' Last name: ' + self.last_name + ' Age: ' + str(self.age )+ ' Job: ' + self.job + ' Salary: '+ str(self.salary) + ' Bonus: ' + str(self.bonus) + ' Total Salary: ' + str(self.total_salary)

    def displayFullName(self):
        '''Returns an employee's full name'''
        return self.first_name + ' ' + self.last_name

    def apply_bonus(self):
        '''Applying bonus to salary'''
        self.total_salary = self.salary + self.bonus

    def exportInvoice(self):
        file = open(self.first_name + '_' + self.last_name + '_' + 'invoice.txt', 'w')
        file.write('Your invoice is ready\n Name:' + self.displayFullName())
        file.close()