# 5.1.3

l1 = []		# initialize : ilkleme gerekli ( side effect )
for x in range(1,11):
	l1.append(x**2)

print(l1)
print(x)	# x degiskenini tanımlamadıgımız halde for döngüsündeki parametre olarak kalması gereken x hafızada tutuldu : side-effect



# Functional Programming : mat. denklem tanımlayıp kullanmaya benzer bir bicimde programlama, kod yazma.
# Lambda Expressions : isimsiz bir denklem, fonksiyon olarak 

squares = list(map(lambda y : y**2 , range(1,11) ))	# inline statement olarak kaldıgından y parametresini akılda tutmak gibi bir side-effect olusmaz. 
# Ayrıca initialize etmeye gerek kalmadı. Direkt burada l2 olusturuldu ve icerisine atadık.
print(squares)
# print(y)	# Burada hata verir. y is not defined. 



# map : ilk parametre olarak fonksiyon alır( yapılacak işlem), ikincide ise nereye bu fonksiyonun uygulanacagını, map edecegini!
# map, butun bunlardan sonra bir object dondureceginden list() kullanalım.
def f(a):
	return a+4
l2 = [1,4,8]
print(list(map(f , l2) ))
# print(a)	# hata verir. 

# veya lambda ile
print(list(map(lambda a : a + 4 , l2 ) ))



l3 = [z**2 for z in range(1,11)]
print(l3)
# print(z)	# hata verir fakat python2 surumunde burada da z yi tanımlıyor, istenmedigi halde.



l4 = [ (b,c) for b in [1,2,3] for c in [7,2,1] if b!=c ]
print(l4)


# [1,2,3,4]
# [2,3,4,5]
# [3,4,5,6]
# [4,5,6,7] 
m = [0,1,2,3]
for i in range(1,5):
	m.pop(0)
	m.append(i+3)
	print(m)


n = list(map(lambda t : [t, t+1, t+2, t+3] , range(1,5) ) )
print(n)