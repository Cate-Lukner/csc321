# Networking Management Homework 2
### Part 2

1. What is the IP configuration for your computer (i.e. what is the output of the shell command used for this purpose)?  

**Lakeview Dorm Room Network**  
In Fedora, the output of `ifconfig` to check my IP configuration is as follows:
```bash
[catluk@localhost hw2]$ ifconfig
enp2s0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 0c:9d:92:04:dd:8d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 792  bytes 83242 (81.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 792  bytes 83242 (81.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

virbr0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
        ether 52:54:00:7a:50:8b  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.8  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::2602:6004:27fc:5f37  prefixlen 64  scopeid 0x20<link>
        ether ac:67:5d:43:b1:7e  txqueuelen 1000  (Ethernet)
        RX packets 30471  bytes 28140817 (26.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 16577  bytes 3648560 (3.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```  
The output of my function `get_interfaces()` is as follows:
```python
In [12]: hw2.get_interfaces()                                                   
Out[12]: ['lo', 'enp2s0', 'wlp3s0', 'virbr0', 'virbr0-nic']
```
As expected, my `get_interfaces` function lists all the interfaces shown to be configured in the output of `ifconfig`, with the addition of `virbr0-nic`. 

**BU-Student Network**  
Output of ifconfig to see the IP configuration:
```bash
[catluk@localhost hw2]$ ifconfig
enp2s0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 0c:9d:92:04:dd:8d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 614  bytes 66739 (65.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 614  bytes 66739 (65.1 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

virbr0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
        ether 52:54:00:7a:50:8b  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.181.89  netmask 255.255.240.0  broadcast 192.168.191.255
        inet6 fe80::27c7:c271:8fa:8300  prefixlen 64  scopeid 0x20<link>
        ether ac:67:5d:43:b1:7e  txqueuelen 1000  (Ethernet)
        RX packets 5294  bytes 5624716 (5.3 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2588  bytes 551311 (538.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
Output of my `get_interfaces` function:
```python
In [3]: hw2.get_interfaces()                     
Out[3]: ['lo', 'enp2s0', 'wlp3s0', 'virbr0', 'virbr0-nic']
```
The interfaces are listed the same as with my dorm room wifi. 


2. What are the MAC addresses for these interfaces?  

**Lakeview Dorm Room Network**  
The MAC addresses for these interfaces are shown in the output of my function `get_mac`:
```python
In [16]: for interface in hw2.get_interfaces(): 
    ...:     print(f'{interface}: ', hw2.get_mac(interface)) 
    ...:                                                                        
lo:  [{'addr': '00:00:00:00:00:00', 'peer': '00:00:00:00:00:00'}]
enp2s0:  [{'addr': '0c:9d:92:04:dd:8d', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
wlp3s0:  [{'addr': 'ac:67:5d:43:b1:7e', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
virbr0:  [{'addr': '52:54:00:7a:50:8b', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
virbr0-nic:  [{'addr': '52:54:00:7a:50:8b', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
```

**BU-Student Network**  
The following is the output showing the MAC addresses for each interface:
```python
In [5]: for interface in hw2.get_interfaces(): 
   ...:     print(f'{interface}: ', hw2.get_mac(interface)) 
   ...:      
   ...:                                                                         
lo:  [{'addr': '00:00:00:00:00:00', 'peer': '00:00:00:00:00:00'}]
enp2s0:  [{'addr': '0c:9d:92:04:dd:8d', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
wlp3s0:  [{'addr': 'ac:67:5d:43:b1:7e', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
virbr0:  [{'addr': '52:54:00:7a:50:8b', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
virbr0-nic:  [{'addr': '52:54:00:7a:50:8b', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]
```
The MAC addresses are the same as my dorm room network. 

3. What are the IPv4 and IPv6 addresses associated with these interfaces?  

**Lakeview Dorm Room Network**  
```python
In [21]: for interface in hw2.get_interfaces(): 
    ...:     print(f'{interface}: ', hw2.get_ips(interface)) 
    ...:                                                                        
lo:  {'v4': IPv4Address('127.0.0.1'), 'v6': IPv6Address('::1')}
enp2s0:  None
wlp3s0:  {'v4': IPv4Address('192.168.1.8'), 'v6': IPv6Address('fe80::2602:6004:27fc:5f37')}
virbr0:  {'v4': IPv4Address('192.168.122.1'), 'v6': None}
virbr0-nic:  None
```
As you can see, some interfaces do not include IPv6 or IPv4 address objects. 

**BU-Student Network**  
The following output shows the IPv4 and Ipv6 objects on the `BU-Student` network:
```python
In [4]: for interface in hw2.get_interfaces(): 
   ...:     print(f'{interface}: ', hw2.get_ips(interface)) 
   ...:                                                                         
lo:  {'v4': IPv4Address('127.0.0.1'), 'v6': IPv6Address('::1')}
enp2s0:  None
wlp3s0:  {'v4': IPv4Address('192.168.181.89'), 'v6': IPv6Address('fe80::27c7:c271:8fa:8300')}
virbr0:  {'v4': IPv4Address('192.168.122.1'), 'v6': None}
virbr0-nic:  None
```
The main differences between the BU-Student network and my dorm room network is the interface wlp3s0 addresses. 

4. What are the IPv4 and IPv6 netmasks of each of these IP subnets?  

**Lakeview Dorm Room Network**  
The output of my function `get_netmask` displays the following netmasks for each of these IP subnets:
```python
In [27]: for interface in hw2.get_interfaces(): 
    ...:     print(f'{interface}: ', hw2.get_netmask(interface)) 
    ...:      
    ...:                                                                        
lo:  {'v4': IPv4Address('255.0.0.0'), 'v6': IPv6Address('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')}
enp2s0:  None
wlp3s0:  {'v4': IPv4Address('255.255.255.0'), 'v6': IPv6Address('ffff:ffff:ffff:ffff::')}
virbr0:  {'v4': IPv4Address('255.255.255.0'), 'v6': None}
virbr0-nic:  None
```
As with before, some interfaces do not have netmasks for IPv4 or IPv6 subnets.   

**BU-Student Network**  
The following output displayers the netmasks for each interface:
```python
In [6]: for interface in hw2.get_interfaces(): 
   ...:     print(f'{interface}: ', hw2.get_netmask(interface)) 
   ...:                                                                         
lo:  {'v4': IPv4Address('255.0.0.0'), 'v6': IPv6Address('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')}
enp2s0:  None
wlp3s0:  {'v4': IPv4Address('255.255.240.0'), 'v6': IPv6Address('ffff:ffff:ffff:ffff::')}
virbr0:  {'v4': IPv4Address('255.255.255.0'), 'v6': None}
virbr0-nic:  None
```
As with the IP address objects, the interface that shows a difference between my dorm room network and the BU-Student network is the `wlp3s0` interface.  


5. What are the IPv4 and IPv6 networks associated with each of these addresses?  

**Lakeview Dorm Room Network**  
The output of my function `get_network` displays the following networks associated with each address:
```python
lo:  {'v4': IPv4Network('127.0.0.1/32'), 'v6': IPv6Network('::1/128')}
enp2s0:  None
wlp3s0:  {'v4': IPv4Network('192.168.1.8/32'), 'v6': IPv6Network('fe80::2602:6004:27fc:5f37/128')}
virbr0:  {'v4': IPv4Address('192.168.122.1'), 'v6': None}
virbr0-nic:  None
```

**BU-Student Network**  
The output of my function `get_network` on the BU-Student network displays the following networks associated with each address:
```python
In [7]: for interface in hw2.get_interfaces(): 
   ...:     print(f'{interface}: ', hw2.get_network(interface)) 
   ...:                                                                         
lo:  {'v4': IPv4Network('127.0.0.1/32'), 'v6': IPv6Network('::1/128')}
enp2s0:  None
wlp3s0:  {'v4': IPv4Network('192.168.181.89/32'), 'v6': IPv6Network('fe80::27c7:c271:8fa:8300/128')}
virbr0:  {'v4': IPv4Address('192.168.122.1'), 'v6': None}
virbr0-nic:  None
```
Again, the `wlp3s0` shows the only difference between my dorm room network and the BU-Student network. 
