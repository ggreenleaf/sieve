def sieve (n):
	num_dict = dict([num,True] for num in xrange(1,n+1))

	for i in xrange(2, int(n**.5) + 1 ):
		if num_dict [i]:
			for j in xrange(i*2,n+1,i):
				num_dict[j] = False
	


	return [i for i in xrange(1,n+1) if num_dict[i]]

while True:
	num = raw_input ("Enter a number or end to quit: ")
	
	try:
		int(num)
		print sieve(int(num))
	
	except ValueError:
		if num.lower() == "end":
			break
		else:
			print ("Not a valid number please re-enter")
	
