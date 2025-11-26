#!/usr/bin/bash

declare j=0

for(( i=0; i<20; i++)); do
	((i%2==0)) && ((j=j+3))
echo "i=$i j=$j"
	if (( j>65 && i%2==1)); then
	break
	echo "i=$i j=$j"
	fi
done

