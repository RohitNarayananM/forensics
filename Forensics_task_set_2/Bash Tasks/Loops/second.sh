read n
for i in $(seq 1 $n)
do
	l=` expr $i\*2-1`
	for j in $(seq $i $n)
	do
		printf " "
	done
	for ((j=1; j<=l; j++))
	do
		printf "#"
	done
	for j in $(seq $i $n)
	do
		printf " "
	done
	printf "\n"
done
