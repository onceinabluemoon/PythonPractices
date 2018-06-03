import recursivefunc

print("fib(3) : ", recursivefunc.fibo(3))


num = int(input("Number : "))
print("\n")



# verilen sayıya kadar ki fibonacci sayılarının toplamı
ftoplam=0

a,b=0,1
flist=[]
while (num>b):
	flist.append(b)
	ftoplam+=b
	a, b = b, a+b

print("fibonacci list : ", flist)
print("fibonacci toplamı : ", ftoplam)



print("\n")

# verilen sayıya kadar ki asalların toplamı
plist=[]
ptoplam=0
for s in range(2,num):
	for i in range(2,s):
		if (s%i==0):
			break
	else:
		plist.append(s)
		ptoplam+=s

print("Prime List : ", plist)
print(num, "sayısından küçük asal sayıların toplamı : ", ptoplam)
print(plist[len(plist)-1])


# Verilen sayıdan kücük ilk asal sayıyı bul

for sayi in range(num-1,1,-1):
	for j in range(2,sayi):
		if(sayi%j==0):
			break
	else:
		print(str(num),"sayısının içindeki en büyük asal sayı : ",sayi)
		break

