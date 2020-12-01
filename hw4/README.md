# Homework 4: DNS
### Networking Fall 2020  
### Catherine Lukner  

**FORWARD DNS**
I used the following command to extract the domains and do the forward dns lookup by taking the second column from domains.tsv, removing the header, and running nslookup on each domain. 
```bash
cut -f2 domains.tsv | tail -n +2 | nslookup > forward_dns.txt
```

**REVERSE DNS**
I used the following command to grep the ipv4 and ipv6 addresses out of the forward dns lookup output. I then did a nslookup for each ip address and saved the output to reverse_dns.txt.
```bash
grep 'Address: ' forward_dns.txt | cut -d\   -f2 | nslookup > reverse_dns.txt
```

**GRAPH**
To create the graph, I wrote the bash script that maped the original domains to the domains found in the format I needed. The script is as follows and saved in the file `dnssearch.sh`:
```bash
# Extract the domain names
cut -f2 domains.tsv | tail -n +2 > domains.txt

# Loop through every original domain
while read p; do 
    # Perform a forward dns lookup for each domain, then a reverse dns lookup, and save as an array
    found=( $(nslookup "$p" | grep 'Address: ' | cut -d\   -f2 | nslookup | grep 'name = ' | cut -d\  -f3) )
    # Loop through every domain found in the reverse dns 
    for i in "${found[@]}" 
    do
        # Add a line to the map text file with the original domain
        # mapped to the domain found in the reverse dns lookup
        echo "\"$p\" -> \"$i\";" >> dumap.txt
    done
done <domains.txt

# Remove any duplicate domain -> reverse dns domains
cat dumap.txt | uniq -u > map.txt
rm dumap.txt
```

To create the graph, I copied and pasted the contents of map.txt and added the following lines to the top and bottom of the file `domains_graph.gv`.
Lines added per GraphViz syntax:  
```
digraph domains {
    # map.txt content
}
```

Finally, to create the visualization of the graph with GraphViz, I used `sfdp` in the following command since the graph was quite large. 
`sfdp -Tpng domains_graph.gv -o domains_visual.png`  

The final product can be viewed in the `.png` file `domains_visual.png`. 
