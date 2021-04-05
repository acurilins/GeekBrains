a = float(input('Enter the first day result (km) : '))
b = float(input('Enter the target result (km) : '))
counter = 0

while a <= b:
    print("%.2f" % a)
    a = a + (a / 100 * 10)
    counter = counter + 1
    if a >= b:
        print("Target will be reached on day: ", counter)
