def facto(n):
	if (n==0):
		return 1
	return n * facto(n-1)

# n = int(input(" Number : "))
# print(str(n) + "! = " + str(facto(n)))


def fibo(n):
	if (n==0):
		return 0
	elif(n==1):
		return 1
	return fibo(n-1)+fibo(n-2)


# print("8.Fibonacci : " + str(fibo(8)))
