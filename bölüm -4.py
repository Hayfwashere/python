print("""

Sİsteme hoş geldiniz

1-Fahrenheittan dan Santigrat 

2-Santigrattan Fahrenheit 

3-Yazı çevirme

4-Fibonacci Serisi

5-Çarpım Tablosu

6- kare ve küp alma
Çıkmak için q ya basınız

""")



while True:
    islem = input("Lütfen bir islem giriniz:")
    if(islem=="q"):
        print("Sistemden Cıkılıyor")
        break

    elif(islem=="1"):
        deger=int(input("Lütfen Hesaplamak İstediginiz Değeri giriniz"))
        F = int(deger) *(9/5) + 32
        print(F,"Fahrenheittir.")

    elif(islem=="2"):
        deger = int(input("Lütfen Hesaplamak İstediginiz Değeri giriniz"))
        C = (5 / 9) * (int(deger) - 32)
        print(C, "Santigrattır.")
    elif (islem == "3"):
        deger = input("Lütfen Ters çevirmek  İstediginiz Değeri giriniz")

        print(deger[::-1])
    elif (islem == "4"):
        ilk_sayı = 1

        ikincisayi = 1

        fibonacci = [ilk_sayı, ikincisayi]
        for i in range(10):
            if(ikincisayi<34):
                ilk_sayı, ikincisayi = ikincisayi, ilk_sayı + ikincisayi
                fibonacci.append(ikincisayi)

        print(fibonacci)
    elif (islem == "5"):
        carpim = int(input("Lütfen sayı giriniz:"))

        for i in range(1, 11):
            print(i, "x", carpim, "=", i * carpim)
    elif (islem == "6"):
        liste = []

        for i in range(1, 21):
            if (i % 2 == 0):
                liste.append(i ** 2)
            else:
                liste.append(i ** 3)

        print(liste)

    else:
        print("Hatalı işlem girdiniz!")