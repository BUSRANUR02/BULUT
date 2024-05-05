#1: 1-100 arası üretilecek bir sayaıyı aşağı yukarı ifadeleriyle buldurma.
import random
sayi=random.randomint(1,100)
hak=5
while hak>0:
    hak-=1
    tahmin=int(input('tahmin: '))
    if sayi ==tahmin:
        print('tebrikler bildiniz.')
        break
    elif sayi<tahmin:
        print('yukarı.')
    else:
        print('Aşağı')
        if hak==0:
            print(f'hakkınız bitti.Tutulan sayı:{sayi}')
        

