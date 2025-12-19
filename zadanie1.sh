#!/usr/bin/bash 

for ((i=75; i<=1512; i++)); do
    if (( i % 100 == 0 && i % 200 != 0 )); then
        echo $i
    fi
done

