

from netmiko import ConnectHandler


R1 = { 
        'device_type':'cisco_ios',
        'username': 'admin',
        'secret': 'cisco123',
        'password': 'cisco123',
        'ip':'10.0.0.2'
      }

filepath = input('Input Inventory file backup path: ')
c = ConnectHandler(**R1)
c.enable()
# print(c.send_command('show run'))


host   = c.send_command('show version', use_textfsm=True)[0]['hostname']
output = c.send_command('show run')

with open(f'{filepath}/{host}', 'w')as f:
    f.write(output)
    print(f'The running configuration of {host} has been backed up!!')
