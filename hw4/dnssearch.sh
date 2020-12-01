cut -f2 domains.tsv | tail -n +2 > domains.txt

while read p; do 
    found=( $(nslookup "$p" | grep 'Address: ' | cut -d\   -f2 | nslookup | grep 'name = ' | cut -d\  -f3) )
    for i in "${found[@]}" 
    do
        echo "\"$p\" -> \"$i\";" >> dumap.txt
    done
done <domains.txt

cat dumap.txt | uniq -u > map.txt
rm dumap.txt