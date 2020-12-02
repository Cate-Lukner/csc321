# Networking Final Project Fall 2020
## Author: Catherine Lukner
  
### Part 1
I used the following commands to do packet capturing with tcpdump on the weather updates exercsie:
```bash
tcpdump -s 0 -i eth0 -w wuserver.pcap # On node00
tcpdump -s 0 -i eth0 -w wuclient.pcap # On node01
```

I used the following commands to do packet capturing with tcpdump on the weather updates exercsie:
```bash
tcpdump -s 0 -i eth0 -w taskvent.pcap # On node00
tcpdump -s 0 -i eth0 -w taskwork.pcap # On node01
tcpdump -s 0 -i eth0 -w tasksink.pcap # On node02
```

### Part 2

To combine everything into a single file, I used mergecap in the following command:
```bash
mergecap -w full-take.pcap taskvent.pcap taskwork.pcap tasksink.pcap wuserver.pcap wuclient.pcap
```

To parse out the parts relevant to the weather and task exercises, I used editcap to filter by packet number. I ran the following bash commands to achieve this:
```bash
editcap -r full-take.pcap weather.pcap 1-225
editcap -r full-take.pcap task.pcap 226-14776
```