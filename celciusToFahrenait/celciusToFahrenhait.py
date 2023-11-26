def fahrenheit_hesaplama(celcius):
    
    fahrenhait = 32+(celcius*1.8)
    return fahrenhait

celcius1 = int(input("Celcius formundaki sıcaklık derecesini giriniz : "))
print(fahrenheit_hesaplama(celcius1))
