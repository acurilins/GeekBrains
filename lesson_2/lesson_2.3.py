a = int(input("Enter month of the year in digits (1 to 12): "))

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

seasons = ['winter', 'spring', 'summer', 'autumn']

if a in months:
    print(f'{a}-month of the year is {months[a]}')
    # if a == 1 or 2 or 12:
    if a < 3 or a > 11:
        print(f'and it is {seasons[0]}')
    # elif a == 3 or 4 or 5:
    elif 2 < a < 6:
        print(f'and it is {seasons[1]}')
    # elif a == 6 or 7 or 8:
    elif 5 < a < 9:
        print(f'and it is {seasons[2]}')
    # elif a == 9 or 10 or 11:
    elif 8 < a < 12:
        print(f'and it is {seasons[3]}')     
else:
    print('Error. Please try again.')