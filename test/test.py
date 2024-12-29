# Şekil çizme uygulaması




def kare_ciz(boyut):
    for i in range(boyut):
        print("* " * boyut)


def kalp_ciz(boyut):
    for i in range(boyut // 2, boyut + 1, 2):
        print(" " * ((boyut - i) // 2) + "*" * i + " " * (boyut - i) + "*" * i)
    for i in range(boyut, 0, -1):
        print(" " * (boyut - i) + "*" * (2 * i - 1))


def menu():
    print("\nŞekil Çizme Programı")
    print("1. Üçgen Çiz")
    print("2. Kare Çiz")
    print("3. Kalp Çiz")
    print("4. Çıkış")
    secim = input("Bir seçenek seçin (1-4): ")
    if secim.isdigit() and 1 <= int(secim) <= 4:  # Doğrulama
        return int(secim)
    else:
        print("Geçersiz seçenek, lütfen 1 ile 4 arasında bir sayı girin.")
        return None


while True:
    secim = menu()
    if secim is None:  # Geçersiz giriş olduğunda menüyü tekrar gösterir.
        continue
    if secim == 1:
        print("\nÜçgen:")
        ucgen_ciz()
    elif secim == 2:
        print("\nKare:")
        kare_ciz()
    elif secim == 3:
        print("\nKalp:")
        kalp_ciz()
    elif secim == 4:
        print("Programdan çıkılıyor...")
        break
