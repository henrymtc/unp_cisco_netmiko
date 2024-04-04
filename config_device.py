config_command = [

    'no logging host 192.168.5.37',
    'no logging host 192.168.5.37 transport udp port 1514',
    'ntp server 192.168.3.23',
    'clock timezone UTC -5',
    'logging console warnings',
    'logging history informational',
    'logging monitor notifications',
    'logging host 192.168.3.39 transport udp port 1514',
    'logging trap debugging',
    'logging origin-id ip',
    'logging source-interface vlan 2',
    'logging facility local6',
    'service sequence-numbers',
    'service timestamps log datetime localtime',
    'no ip http server',
    'no ip domain lookup',
    'ip name-server 192.168.3.3',
    'snmp-server community Un1N4cP1ur4 RO',
    'do write memory'

]