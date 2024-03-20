'''Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.'''

boycm = int(input("Lütfen boyunuzu (santimetre cinsinde) girin: "))
ağirlik = int(input("Lütfen ağırlığınızı (kilogram cinsinde) girin: "))

boym = boycm / 100

vki = ağirlik / (boym * boym)

print("Vücut Kitle İndeksiniz (VKİ):", vki)

'''Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.'''

maas= int(input('lütfen maasinizi giriniz: '))
zamOrani= int(input('lütfen zam oraninizi giriniz: '))
employee= maas+(maas*(zamOrani/100))
print ('yeni maaşınız=',employee)

'''Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.'''

sayi1= int(input('lütfen 1.sayyıyı giriniz= '))
sayi2= int(input('lütfen 2.sayıyı giriniz='))
sayi3= int(input('lütfen 3.sayıyı giriniz= '))
enbüyük = sayi1

if sayi2 > sayi1:
    enbüyük = sayi2

if sayi3 > sayi2:
    enbüyük = sayi3

print("En büyük sayı:", enbüyük)

'''Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)'''

sayi = input("Lütfen bir sayi giriniz: ")

tersten = sayi[::-1]

if sayi == tersten:
    print("Bu sayi bir palindromdur.")
else:
    print("Bu sayi bir palindrom değildir.")

'''Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.'''

yariçap = float(input("Dairenin yarıçapını girin: "))

import math
alan = math.pi * yariçap ** 2


çevre = 2 * math.pi * yariçap


print("Dairenin Alanı:", alan)
print("Dairenin Çevresi:", çevre)

sayi = input("Lütfen bir sayi giriniz: ")

tersten = sayi[::-1]

if sayi == tersten:
    print("Bu sayi bir palindromdur.")
else:
    print("Bu sayi bir palindrom değildir.")

