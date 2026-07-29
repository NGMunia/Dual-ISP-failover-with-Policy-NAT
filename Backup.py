

from Network_devices.devices import routers, firewalls, gateway
from netmiko import ConnectHandler
from csv import writer
from itertools import chain




filepath = input('select the backup folder path for all your Startup Configurations: ')

for devices in chain(routers.values(), firewalls.values(), gateway.values()):   
    c = ConnectHandler(**devices)
    c.enable()
# print(c.send_command('show run'))

    host   = c.send_command('show version', use_textfsm=True)[0]['hostname']
    output = c.send_command('show startup-config')

    with open(f'{filepath}/{host}', 'w')as f:
        f.write(output)
        print(f'The start-Up configuration of {host} has been backed up!!')

