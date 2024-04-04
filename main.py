from netmiko import ConnectHandler
import Auth
import config_device

net_connect = ConnectHandler(**Auth.cisco_2_91)
net_connect.enable()
output = net_connect.send_config_set(config_device.config_command)
print(output)
