print('*' * 15, 'Calculator', '*' * 15)
print('For exit press q')

while True:
    s = input('Sign (+, -, * or / ): ')
    if s == 'q': break
    if s in ('+', '-', '*', '/'):
        x = float(input('x = '))
        y = float(input('y = '))
        if s == '+':
            print('%.2f' % (x+y))
        elif s == '-':
            print('%.2f' % (x-y))
        elif s == '*':
            print('%.2f' % (x*y))
        elif s == '/':
            if y != 0:
                print('%.2f' % (x/y))
            else:
                print('Division by zero!')
else:
    print('Wrong operation sigh!')