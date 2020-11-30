I copied over the files:
docker cp wuserver.py final_node00_1:/wuserver.py
docker cp wuclient.py final_node01_1:/wuclient.py

To do packet capture:
tcpdump -s 0 -i eth0 -w wuserver.pcap
tcpdump -s 0 -i eth0 -w wuclient.pcap

docker cp taskvent.py final_node00_1:/taskvent.py
docker cp taskwork.py final_node01_1:/taskwork.py
docker cp tasksink.py final_node02_1:/tasksink.py

docker cp final_node00_1:/taskvent.pcap taskvent.pcap
docker cp final_node01_1:/taskwork.pcap taskwork.pcap
docker cp final_node02_1:/tasksink.pcap tasksink.pcap

Combined everything using:
mergecap -w full-take.pcap taskvent.pcap taskwork.pcap tasksink.pcap wuserver.pcap wuclient.pcap

To read the pcap in a friendly format, I ran the following command:
tcpdump -qns 0 -X -r serverfault_request.pcap