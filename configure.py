
from netmiko import ConnectHandler
from Network_devices.devices import routers, firewalls, gateway
from itertools import chain


##Configuring IP helper address

# for devices in chain(routers.values()):
#     c = ConnectHandler(**devices)
#     c.enable()

#     commands = ['interface e0/0',
#                 'ip helper-address 10.21.0.2']
    
#     print(c.send_config_set(commands))
#     c.save_config()
#     c.disconnect()



## COnfiguring SNMP on all devices:

# for devices in chain(routers.values(), firewalls.values(),gateway.values()):
#     c = ConnectHandler(**devices)
#     c.enable()

#     host = c.send_command('show version', use_textfsm=True)[0]['hostname']

#     snmp_intf = input(f'Selecet the SNMP source interface for {host}: ')

#     commands = ['ip access-list standard SNMP-ACL',
#                 'permit 192.168.21.100',
#                 'process cpu threshold type total rising 80 interval 60 falling 60 interval 60',
#                 f'snmp-server source-interface traps {snmp_intf}',
#                 'snmp-server enable traps config',
#                 'snmp-server enable traps ospf',
#                 'snmp-server enable traps cpu',
#                 'snmp-server enable traps memory',
#                 f'snmp-server chassis-id {host}',
#                 'snmp-server community DEVICE-SNMP SNMP-ACL',
#                 'snmp-server host 192.168.21.100 version 2c DEVICE-SNMP'
#                 ]
#     print(c.send_config_set(commands),'\n')


# for devices in chain(routers.values(), firewalls.values(), gateway.values()):
#     c = ConnectHandler(**devices)
#     c.enable()

#     commands = ['ip access-list extended VTY-ACL',
#                 'permit tcp 192.168.10.0 0.0.0.255 any eq 22',
#                 'permit tcp 192.168.21.0 0.0.0.255 any eq 22',
#                 'deny tcp any any log',
#                 'line vty 0 4',
#                 'access-class VTY-ACL in'
#                 ]
#     print(c.send_config_set(commands),'\n')
#     c.save_config()
#     c.disconnect()


## CONFIGURING QoS ON LAN ROUTERS
# for devices in chain (routers.values()):
#     c = ConnectHandler(**devices)
#     c.enable()

#     commands = ['policy-map INTERNET-POLICY',
#                 'class class-default',
#                 'police cir 5000k conform-action transmit exceed-action drop',
#                 'interface e0/0',
#                 'service-policy input INTERNET-POLICY',
#                 'service-policy output INTERNET-POLICY']
    
#     print(c.send_config_set(commands))
#     c.save_config()
#     c.disconnect()
