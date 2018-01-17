
a=1
b=1
dizi=[a,b]
for i in range(10):
    a,b= b,a+b
    dizi.append(b) #burda a'yý almaya gerek yok #
print(dizi)