my_file = "lesson_5.5.txt"
numbers = "0 1 2 3.14 99"
sum = 0

try:
    with open(my_file, 'w') as fhs:
        fhs.write(numbers)

    with open(my_file, 'r') as fhd:
        data = fhd.read()

    for item in data.split():
        sum += float(item)
except IOError as e:
    print(e)
except ValueError:
    print("Error!")

print(sum)
