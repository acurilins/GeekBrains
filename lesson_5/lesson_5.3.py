import sys


min_salary = 20000
my_file = "lesson_5.3.txt"

try:
    with open(my_file, 'r') as fh:
        employees = fh.readlines()
except IOError as e:
    print(e)
    sys.exit(1)

sum_salary = 0

for employee in employees:
    name, salary = employee.split()

    try:
        salary = float(salary)
    except ValueError:
        continue

    sum_salary += salary
    if salary < min_salary:
        print(name)

print('Average salary is: ', round(sum_salary / len(employees), 2))
