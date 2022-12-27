from random import randint

secim= input("Sınavın hesabı için:(1),VKİ hesabı için:(2),Dikdörtgen alan hesabı için:(3),Maaş hesaplamak için:(4),Sayı Tahmin oyunu için:(5) Tuşlayınız:")
if secim == "1":
    vize = input('Vize Notunuz : ')
    final = input('Final Notunuz : ')
    ortalama=(float(vize)*0.3)+(float(final)*0.7)
    print("Ortalama :{0} ".format(ortalama))
    if(int(ortalama)>=60):
        print("Geçtiniz")
    else:
        print("Kaldınız")
elif secim == "2":
    print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI 💪")
    boy = float(input("Boy (m):"))
    kilo = int(input("Kilo (kg):"))
        
    endeks  = kilo/(boy*boy)
        
    if endeks <=18:
        print("\n zayıf VKİ:{}".format(endeks))
    elif endeks > 18 and endeks <=25 :
        print("\n kilolu VKİ:{}".format(endeks))
    elif endeks > 25 and endeks <=30:
        print("\n obez VKİ:{}".format(endeks))
    elif endeks > 30:
        print("\n ciddi obez VKİ:{}".format(endeks))

elif secim== "3":
    kisa=input('Kısa Kenar : ')
    uzun=input('Uzun Kenar : ')
    alan=int(kisa)*int(uzun)
    cevre=2*(int(kisa)+int(uzun))
    print("Alan : {0}".format(alan))
    print("Çevre : {0}".format(cevre))

elif secim == "4":
    maas = input("Aldığınız ücret: ")
    calısma_gunu = input("Çalıştığınız gün sayısı:")
    Alinanmaas=int(maas)/30 * int(calısma_gunu)
    print("alacağınız ücret:",Alinanmaas)

elif secim == "5":
    rand=randint(1, 100)
    sayac=0
        
    while True:
        sayac+=1
        sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
        if(sayi==0):
            print("Oyunu İptal Ettiniz")
            break
        elif sayi < rand:
            print("Daha Yüksek Bir Sayı Girin.")
            continue
        elif sayi > rand:
            print("Daha Düşük Bir Sayı Girin.")
            continue
        else:
            print("Rastele seçilen sayı {0}!".format(rand))
            print("Tahmin sayınız {0}".format(sayac))
else:
    print("seçiminizde işlem bulunmamaktadır!!")