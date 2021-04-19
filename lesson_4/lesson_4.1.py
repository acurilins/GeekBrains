from sys import argv

salary, hours, rate, bonus = argv

calc = (float(hours) * float(rate)) + float(bonus)
print(f"Gross Salary:\n{calc}")
