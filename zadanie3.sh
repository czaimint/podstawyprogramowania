#!/usr/bin/bash

declare -a tab=(2 6 9 22 66 420)
declare -a t=(1 5 18 67 44 24)

len=${#tab[@]}

#rosnacy
for ((i=0; i<len; i++));do
    for ((j=0; j<len-i-1; j++));do
        if (( tab[j] > tab[j+1] ));then
            temp=${tab[j]}
            tab[j]=${tab[j+1]}
            tab[j+1]=$temp
        fi
    done
done
echo "${tab[@]}"

#malejacy
for ((i=0; i<len; i++));do
    for ((j=0; j<len-i-1; j++));do
        if (( t[j] < t[j+1] ));then
            temp=${t[j]}
            t[j]=${t[j+1]}
            t[j+1]=$temp
        fi
    done
done
echo "${t[@]}"

