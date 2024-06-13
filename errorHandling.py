liste=["1","2","5a","10b","abc","10","50"]
#1:liste elemanları içindeki sayısal değerleri bulma

for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue
#2: kullanıcı"q" değerini girmedikçe aldığımız her inputun sayı olup olmadığını kontrol etme

while True:
    sayi=input('sayı:')
    if sayi=='q':
        break
    try:
        result=float(sayi)
        print('girdiğiniz sayı:',result)
        break
    except ValueError:
        print('geçersiz sayi')
        contunie

#3:Girilen parola içinde türkçe karakter hatası verme
turkce_karakterler='şçğüöıİ'
parola=input('parola')
for i in parola:
    if i in turkce_karakterler:
        raise TypeError('Parola türkçe karakter içeremez.')
    else:
        pass
    print('geçerli parola')
  #4:faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verme
def faktoriyel(x):
    x=int(x)
    if x<0:
        raise ValueError('Negatif değer')
    result=1
    for i in range(1,x+1):
        result*=i
        return result
    for x in[5,10,20,-3,'10a']:
        try:
            y=faktoriyel(x)
        except ValueError as err:
            print(err)
            continue
       print(y)
