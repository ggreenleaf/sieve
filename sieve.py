def sieve (n):
	num_dict = dict([num,True] for num in range(1,n+1))

	for i in range(2, int(n**.5) ):
		if num_dict [i]:
			for j in range(i*2,n+1,i):
				num_dict[j] = False
	


	return [i for i in range(1,n+1) if num_dict[i]]

while True:
	num = raw_input ("Enter a number or end to quit: ")
	if num.lower() == "end":
		break;
	else:
		print sieve(int(num))
