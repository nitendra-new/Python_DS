#
# Program to find number of primes less than or equal to n
# using sieve  of eratosthenes

import sys
import math
import random


def countPrimes(num):
	isPrime = [True]*(num+1)

	for i in range(2,num):
		if isPrime[i]:
			j = 2
			while (i*j) <= num:
				isPrime[i*j] = False
				j += 1
	count = 0
	for i in range(2,num+1):
		if isPrime[i]:
			count += 1
	return count

print (countPrimes(int(sys.argv[1])))
