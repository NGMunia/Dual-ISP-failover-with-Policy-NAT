

from login import username, password, secret


routers =   {  
                 'R1' : {'device_type': 'cisco_ios',
                         'username': username,
                         'password': password,
                         'secret': secret,
                         'ip': '192.168.10.1'
                         },
                 'R2' : {'device_type': 'cisco_ios',
                         'username': username,
                         'password': password,
                         'secret': secret,
                         'ip': '192.168.11.1'
                         },
                 'R3' : {'device_type': 'cisco_ios',
                         'username': username,
                         'password': password,
                         'secret': secret,
                         'ip': '192.168.12.1'
                         }
              }
firewalls =   {
                'fw1' : {'device_type': 'cisco_ios',
                         'username': username,
                         'password': password,
                         'secret': secret,
                         'ip': '192.168.21.1'
                         },
                'fw2' : {'device_type': 'cisco_ios',
                         'username': username,
                         'password': password,
                         'secret': secret,
                         'ip': '10.48.0.2'
                         }
              }
gateway =     {  'R1': {
                       'device_type': 'cisco_ios',
                       'username': username,
                       'password': password,
                       'secret': secret,
                       'ip': '10.48.0.6'
                       }
              }