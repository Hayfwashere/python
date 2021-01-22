
print("******************1-SORU*******************")

bitcoin = 1000
i=1
oran = 0.12
while True:
    if(i==8):
        break
    else:
        bitcoin = bitcoin + bitcoin*oran
    i +=1
print("Toplam Paramız:",bitcoin)


print("******************2-SORU*******************")

print("Hafta başında 1000 dolarlık bitcoin aldığımızda günde ortalama %"+str(oran*100) + "kazançla, bir hafta sonunda " +str(bitcoin-1000) +" dolar kazanırdık")

print("*******************3-SORU************************")

dosya_adi=input("Dosya Adı Giriniz :")
print("Girilen dosya adi: "+dosya_adi+".py")