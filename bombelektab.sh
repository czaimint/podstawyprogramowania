#!/usr/bin/bash

declare -a table=(100 12 9 70 16 0 81)

echo ${table[@]}

t= ${table[@]}

for (( i=0; i<t-1; i++ )); do
        for(( j=0; i<z-1-i; j++ )); do
                if [[ ${table[j]} -gt ${table[j+1]} ]]; then
                        buf= ${table[j]}
                        table[j]= ${table[j+1]}
                        table[j+1]= $buf
                fi
        done
done

echo "Posortowana tablica: ${table[@]}"
