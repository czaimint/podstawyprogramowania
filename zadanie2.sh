#!/usr/bin/bash

read -p "podaj poczatek: " start
read -p "podaj koniec: " stop

count=0
i=$start

while (( i <= end )); do
	if (( i % 3 == 0 )); then
		((count++))
		if (( count % 2 == 0 )); then
			echo "$i"
		 fi
	fi
	((i++))
done
