import random  # Bilgisayarın rastgele sayı seçebilmesi için bu kütüphaneyi çağırıyoruz.

# Bilgisayar 1 ile 20 arasında rastgele bir sayı tutuyor
gizli_sayi = random.randint(1, 20)

print("🤖: 1 ile 20 arasında bir sayı tuttum. Hadi tahmin et!")

# Oyuncu doğru bilene kadar oyunun devam etmesi için bir döngü başlatıyoruz
while True:
    # Oyuncudan tahmin alıyoruz
    tahmin = int(input("Senin Tahminin: "))

    # Tahminleri kontrol ediyoruz
    if tahmin == gizli_sayi:
        print("🎉 Tebrikler! Doğru bildin!")
        break  # Doğru bilindiği için 'break' komutuyla döngüyü bitiriyoruz.
    elif tahmin < gizli_sayi:
        print("📉 Biraz daha BÜYÜK bir sayı söyle.")
    else:
        print("📈 Biraz daha KÜÇÜK bir sayı söyle.")