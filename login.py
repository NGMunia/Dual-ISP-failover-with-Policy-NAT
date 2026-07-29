
from getpass import getpass

username = input('Username: ')
password = getpass('password: ')
secret   = getpass('secret: ')

while True:
    if username == 'Automation' and password == 'cisco123' and secret == 'cisco123':
        print('Login successful!')
        break
    else:
        print('USername and/or password incorrect!')
        username = input('Username: ')
        password = getpass('password: ')
        secret   = getpass('secret: ')

