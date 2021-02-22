read n
for i in $(seq 1 $n)
do
	for j in $(seq $i $n)
	do
		printf " "
	done
	for j in $(seq 1 $i)
	do
		printf "#"
	done
	printf "\n"
done
