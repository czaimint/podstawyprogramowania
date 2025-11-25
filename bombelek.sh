#!/usr/bin/bash

declare -a tablica=(100 12 9 70 16 0 81)

tablica[7]=2137
tablica[8]=420
tablica[9]=67

echo "${tablica[@]}"

z=${#tablica[@]}

for ((i=0; i<z-1; i++)); do
    for ((j=0; j<z-1-i; j++)); do
        if [[ ${tablica[j]} -gt ${tablica[j+1]} ]]; then
            bufor=${tablica[j]}
            tablica[j]=${tablica[j+1]}
            tablica[j+1]=$bufor
        fi
    done
done

echo "posortowana tablica: ${tablica[@]}"
echo "minimalna liczba: ${tablica[0]}"
