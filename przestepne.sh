<<<<<<< HEAD
#!/usr/bin/bash
=======
read -p "podaj rok: " year

if [[ (year%4 -eq 0 && year%100 -ne 0) && (year%400 -eq 0) ]]; then
	echo "$year jest przestepny"
else
	echo "$year nie jest przestepny"
fi
>>>>>>> bc339cdc626c4da603c45e37908f6e95dc4c96cd
