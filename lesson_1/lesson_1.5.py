inc = int(input('Enter income: '))
exp = int(input('Enter expenses: '))

if inc > exp:
    print('Your business is successful!')
    print('Profit is - ', ((inc-exp)/inc)*100, '%')

    staff = int(input('Enter employees quantity: '))
    print('Profit per employee is - ', ((inc-exp)/inc)*100 / staff, '%')
else:
    print('You have to try harder, guys!')
