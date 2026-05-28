import random

# Bilgisayar 1 ile 100 arasında rastgele bir sayı seçiyor
hedef_sayi = random.randint(1, 100)

print("1 ile 100 arasında bir sayı tuttum. Hadi tahmin et!")

# Kullanıcının kaç kerede bildiğini saymak için
tahmin_sayisi = 0

while True:
    tahmin = int(input("Tahmininiz: "))
    tahmin_sayisi = tahmin_sayisi + 1  # her tahminde sayacı 1 artırıyoruz

    if tahmin < hedef_sayi:
        print("Daha büyük bir sayı söyle!")
    elif tahmin > hedef_sayi:
        print("Daha küçük bir sayı söyle!")
    else:
        print("Tebrikler! Doğru bildiniz.")
        print("Toplam", tahmin_sayisi, "kerede buldunuz.")
        break  # Oyunu bitir ve döngüden çık