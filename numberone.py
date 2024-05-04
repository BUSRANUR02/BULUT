sayilar=[1,3,5,7,9,12,19,21]
#1:sayılar listesini while ile ekrana yazdırma
i=0
while(i<len(sayilar)):
      print(sayilar[i])
      i+=1

#2:başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm değerleri yazdıran program
a=int (input('başlangıç:'))
b=int (input('bitiş:'))
i=a
while i<b:
      i+=1

      print(i)
 #tek sayıları yazdırma
      a=int (input('başlangıç:'))
b=int (input('bitiş:'))
i=a
while i<b:
      i+=1
      if(i%2==1) :

       print(i)
#3:1 ile 100 arasındaki sayıları azalan şekilde yazdırma
 i=100
while(i>0):
    i-=1
    print(i)
#4:kullanıcıdan alınan 5 sayıyı sıralı bir şekilde yazdırma
numbers=[]
i=0
while i<5:
    sayi=int(input('sayi:'))
    numbers.append(sayi)
    i+=1
numbers.sort()
    print(numbers)
#5:Kullanıcıdan alacağımız sınırsız ürün bilgisini ürünler listesi içerisinde saklama
urunler=[]
adet=int(input('kaç ürün eklemek istiyorsunuz:'))
i=0
while(i<adet):
    name=input('ürün ismi:')
    price=input('ürün fiyatı:')
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1
    for urun in urunler:
        print(f'ürün adi:{urun[''name'']}ürün fiyat:{urun[''price'']}')


