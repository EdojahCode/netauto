from netmiko import ConnectHandler
device = {
  'device_type': 'cisco_ios',
  'host': '192.168.10.1',
  'username': 'admin',
  'password': 'cisco'
}
connection = ConnectHandler(**device)
vlans = ['vlan 10', ' SCIENCE_VLAN ', 'exit']
print(connection.send_config_set(vlans))