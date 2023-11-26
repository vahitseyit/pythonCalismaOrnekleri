# emeklilik_hesaplama.py

def emeklilik_yasini_hesapla(dogum_yili, emeklilik_yasi):

    simdiki_yil = 2023  # Örnek olarak 2023 yılı kullanılmıştır.
    kullanici_yasi = simdiki_yil - dogum_yili
    emeklilik_yili = dogum_yili + emeklilik_yasi
    if kullanici_yasi >= emeklilik_yasi:
        return emeklilik_yili, "Zaten emekli olmuşsunuz veya bu yıl emekliliğiniz gerçekleşmiştir."
    else:
        return emeklilik_yili, f"Emekli olmanıza {emeklilik_yili - simdiki_yil} yıl kalmıştır."

# Aşağıdaki fonksiyonlar farklı kullanıcılar için yaş hesaplamayı sağlar.

def kullanici1_emeklilik_hesaplama():
    dogum_yili = int(input("Lütfen doğum yılınızı giriniz: "))
    emeklilik_yasi = int(input("Kaç yaşında emekli olmayı planlıyorsunuz? "))
    emeklilik_yili, mesaj = emeklilik_yasini_hesapla(dogum_yili, emeklilik_yasi)
    print(f"Emeklilik yılınız: {emeklilik_yili}. {mesaj}")



if __name__ == "__main__":
    kullanici1_emeklilik_hesaplama()

