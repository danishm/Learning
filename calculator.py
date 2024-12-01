from decimal import *

keep_on_going = 'y'

while keep_on_going == 'y':
    operation = input('What do you want to do? ')
    if operation in ['a', 's', 'm', 'd']:

        a = Decimal(input('Enter 1st number: '))
        b = Decimal(input('Enter 2nd number: '))

        ans = 0

        if operation == 'a': ans = a + b
        elif operation == 's': ans = a - b
        elif operation == 'm': ans = a * b
        elif operation == 'd': ans = a / b

        print('----------------------------------')
        print('Your answer is: ', ans)
        print('----------------------------------')
    else:
        print ('Please select a correct operation')

    keep_on_going = input("Do you want to continue (y/n): ")
