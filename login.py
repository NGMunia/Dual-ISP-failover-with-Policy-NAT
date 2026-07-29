
from getpass import getpass

username = input('Username: ')
password = getpass('password: ')
secret   = getpass('secret: ')

while True:
    if username == 'Automation' and password == 'cisco123' and secret == 'cisco123':
        print('Login successful!')
        break
    else:
        print('Incorrect Username and/or password, Try Again!')
        username = input('Username: ')
        password = getpass('password: ')
        secret   = getpass('secret: ')

