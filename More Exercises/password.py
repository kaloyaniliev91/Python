username = input()
password = input()

data = input()

if data != password:
    print('Type your password again: ')
    data = input()
else:
    print(f'Welcome {username}!')