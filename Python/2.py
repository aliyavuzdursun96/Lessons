# 1. Kullanıcıdan ilk sayıyı istiyoruz ve bilgisayarın aklında tutması için 'sayi1' isimli bir kutuya koyuyoruz.
# 'int' ifadesi, bilgisayara bunun bir "tam sayı" olduğunu söylüyor.
sayi1 = int(input("İlk sayıyı giriniz: "))

# 2. Kullanıcıdan ikinci sayıyı istiyoruz ve onu da 'sayi2' kutusuna koyuyoruz.
sayi2 = int(input("İkinci sayıyı giriniz: "))

# 3. Bilgisayara işlemlerimizi yaptırıp sonuçları yeni kutulara kaydediyoruz.
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2

# 4. Sonuçları ekrana yazdırıp kullanıcıya gösteriyoruz.
print("--------------------------")
print("Toplama Sonucu:", toplam)
print("Çıkarma Sonucu:", fark)
print("Çarpma Sonucu :", carpim)
print("Bölme Sonucu  :", bolum)
print("--------------------------")