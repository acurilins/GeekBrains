my_file = "lesson_5.6.txt"
subjects = {}

try:
    with open(my_file, 'r') as fh:
        for line in fh.readlines():
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
except IOError as e:
    print(e)
except ValueError:
    print("Error")

print(subjects)

