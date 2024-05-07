#Gönderilen kelimeyi belirtilen kez ekranda yazdıran fonksiyon
def yazdir(kelime,adet):
    print(kelime*adet)
    yazdir("yazdir\n",10)

#kendine gönderilen sayısız parametreyi bir listeye çeviren fonksiyon.
def listeyeCevir(*params):
    liste=[]
    for param in params:
        liste.append(param)
        return liste
    result=listeyeCevir(10,20,30,'merhaba')
    print(result)

#Gönderilen 2 sayı arasındaki tüm asalsayıları bulma

sayi1=int(input("1. sayı:"))
sayi2=int(input("2.sayı:"))
def asalSayilariBul(sayi1,sayi2):
    for sayi in range(sayi,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if (sayi%i==0):
                    break
                else:
                    print(sayi)

                    asalSayilariBul(sayi1,sayi2)


#Kendisine gönderile bir sayının tam bölenlerini bir liste şeklindegönderen fonksiyon.
def tamBölenleriBul(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if (sayi%i==0):
            tamBolenler.append(i)
            return tamBolenler
        print(tamBölenleriBul(20))
