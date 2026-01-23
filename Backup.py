

from netmiko import ConnectHandler
from csv import writer


R1 = { 
        'device_type':'cisco_ios',
        'username': 'admin',
        'secret': 'cisco123',
        'password': 'cisco123',
        'ip':'10.0.0.2'
      }

# backup_filepath = input('Type the backup folder path where device configurations will be stored: ')
# c = ConnectHandler(**R1)
# c.enable()
# # print(c.send_command('show run'))


# host   = c.send_command('show version', use_textfsm=True)[0]['hostname']
# output = c.send_command('show startup-config')

# with open(f'{backup_filepath}/{host}', 'w')as f:
#     f.write(output)
#     print(f'The start-Up configuration of {host} has been backed up!!')




# DEVICES' INVENTORY
print("TAKING NETWORK DEVICES' INVENTORY")
inventory_filepath = input('Type the folder path that will be used to store network device information: ')
with open (f'{inventory_filepath}/Data.csv', 'w')as f:
    write_data = writer(f)
    write_data.writerow(['Hostname','IP address','Software Image','Version','Serial number'])

    c = ConnectHandler(**R1)
    c.enable()
    output = c.send_command('show version',use_textfsm=True)[0]

    hostname = output['hostname']
    ip_addr  = R1['ip']
    image    = output['software_image']
    version  = output['version']
    serial   = output['serial']

    write_data.writerow([hostname,ip_addr,image,version,serial])
    print(f'Finished taking {hostname} Inventory')
    c.disconnect()