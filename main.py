#input_first_name = input('insert first name ')
#input_last_name = input('insert last name ')
#input_age = int(input('insert age '))
#input_job = input('insert job ')
#input_salary = int(input('insert salary '))
#input_bonus = int(input('insert bonus '))


from models.department import Department
from models.employer import Employer

employers = []
departments = []

employer1 = Employer('Vlad', 'Horaicu', 28, 'IT', 6000, 800)
employer2 = Employer('Andrei', 'Gheorghe', 30, 'IT', 7000, 890)
employer3 = Employer('Mircea', 'Andrei', 22, 'IT', 5000, 600)
# applying bonus to Employer instance
employer3.apply_bonus()
employers.append(employer1)
employers.append(employer2)
employers.append(employer3)

# show all employers
for i in employers:
    print(i)

departament1 = Department("Human resources")
departament2 = Department("Research")
departments.append(departament1)
departments.append(departament2)


print('===========Departments==============')
departament1.displayDepartment()
departament1.addEmployer(employer1)
departament1.addEmployer(employer2)

departament1.addEmployer(employer3)
print('before removing 1 employer')
departament1.displayEmployers()
departament1.removeEmployer(employer1)
print('after removing 1 employer')
departament1.displayEmployers()

departament2.displayDepartment()
departament2.addEmployer(employer2)
departament2.displayEmployers()

for i in departament1.employers:
    if i == employer2:
        #apply bonus to employer from department instance
        print(i)
        i.apply_bonus()
        print(i)


# extra exporting invoice
employer1.exportInvoice()