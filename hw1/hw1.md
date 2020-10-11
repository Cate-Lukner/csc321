# Homework 1
### Network Management
### Cate Lukner

## Datalink

1. *How many different things are listed in the output of the arp -a command?*  
I should prefece by saying I am connected to a coffee shop network.  

When I run `arp -a`, four interfaces output. Three of the four interfaces have six IPv4 addresses listed underneath them. The fourth interface has eight IPv4 addresses listed underneath it. All of the addresses are static. Under every interface there are two broadcast addresses listed. 

2. *Start an IPython console (i.e. just type ipython in PowerShell/Termina) in the same directory as netlayers.py. In that console, type the following:*
```python
 import netlayers
 netlayers.arp_table()
```
*What are the different devices connected to your home network? Can you identify what they are based on this information?*  
I am connected to a coffee shop network, so my answer is reflective of this network. 

The output:   
```
In [2]: netlayers.arp_table()
Name  IP               MAC                Company
  ---------------  -----------------  -----------------
  169.254.255.255  ff:ff:ff:ff:ff:ff
  224.0.0.22       01:00:5e:00:00:16
  224.0.0.251      01:00:5e:00:00:fb
  224.0.0.252      01:00:5e:00:00:fc
  239.255.255.250  01:00:5e:7f:ff:fa
  255.255.255.255  ff:ff:ff:ff:ff:ff
  192.168.44.254   00:50:56:ff:7c:ad  VMware, Inc.
  192.168.44.255   ff:ff:ff:ff:ff:ff
  224.0.0.22       01:00:5e:00:00:16
  224.0.0.251      01:00:5e:00:00:fb
  224.0.0.252      01:00:5e:00:00:fc
  239.255.255.250  01:00:5e:7f:ff:fa
  255.255.255.255  ff:ff:ff:ff:ff:ff
  192.168.2.1      00:50:f1:80:00:00  Intel Corporation
  192.168.2.193    00:e1:8c:96:34:76  Intel Corporate
  192.168.2.255    ff:ff:ff:ff:ff:ff
  224.0.0.22       01:00:5e:00:00:16
  224.0.0.251      01:00:5e:00:00:fb
  224.0.0.252      01:00:5e:00:00:fc
  239.255.255.250  01:00:5e:7f:ff:fa
  255.255.255.255  ff:ff:ff:ff:ff:ff
  192.168.197.254  00:50:56:e2:fd:c0  VMware, Inc.
  192.168.197.255  ff:ff:ff:ff:ff:ff
  224.0.0.22       01:00:5e:00:00:16
  224.0.0.251      01:00:5e:00:00:fb
  224.0.0.252      01:00:5e:00:00:fc
  239.255.255.250  01:00:5e:7f:ff:fa
  255.255.255.255  ff:ff:ff:ff:ff:ff
```

At this coffee shop there are multiple laptops, phones, and the coffee shop register connected. From this output information, it seems that there are multiple private devices under one of the three or four routers/switches since I see repeats of the same address (e.g. 224.0.0.22, 224.0.0.252). 

## Network
*Run the following commands in your console.*
```
ping google.com
ping localhost
```
1. *What are the differences between the two commands?*  
In each command, four packets were sent and received. In the ping to the localhost, the round trip times in milli-seconds was 0ms. On the other hand, the ping to google had a minimum round trip of 30ms and a maximum of 33ms with an average of 31ms. The ping to google showed a reply from an IPv4 address while the ping to the localhost showed a reply from an IPv6 address. In terms of differences of the commands' actions, the ping to google.com is sending and recieving packets to a real Google server. The ping to localhost is simply my computer sending and recieving packets to itself. 