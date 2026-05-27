import random

def sayi_tahmin_oyunu():
    # 1 ile 100 arasında rastgele bir sayı seçiyoruz (100 dahil)
    gizli_sayi = random.randint(1, 100)
    tahmin_sayisi = 0
    
    print("=== Sayı Tahmin Oyununa Hoş Geldiniz! ===")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım kaç kerede bulacaksınız?")
    print("--------------------------------------------------")

    # Oyuncu doğru tahmin edene kadar dönecek döngü
    while True:
        try:
            # Kullanıcıdan tahmin alıyoruz
            tahmin = int(input("Tahmininiz nedir?: "))
            tahmin_sayisi += 1  # Her tahminde sayacı 1 artırıyoruz

            # Tahmin kontrolü
            if tahmin < gizli_sayi:
                print("Daha büyük bir sayı girin! ⬆️")
            elif tahmin > gizli_sayi:
                print("Daha küçük bir sayı girin! ⬇️")
            else:
                print(f"\n🎉 Tebrikler! Doğru tahmin! Sayı: {gizli_sayi}")
                print(f"🕵️‍♂️ Toplam {tahmin_sayisi} hamlede sonuca ulaştınız.")
                break # Doğru tahmin edildiğinde döngüden çıkıyoruz
                
        except ValueError:
            # Kullanıcı sayı yerine harf veya geçersiz bir karakter girerse hata vermemesi için
            print("Lütfen sadece tam sayı giriniz!")

# Oyunu başlatıyoruz
sayi_tahmin_oyunu()