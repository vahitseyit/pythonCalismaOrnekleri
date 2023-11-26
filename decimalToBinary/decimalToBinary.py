decimal = int(input("Decimale cevirmek istediğiniz sayiyi giriniz"))
binary = 0
a = 0
gecici = decimal


while gecici > 0:
    binary = ((gecici%2)*(10**a)) + binary
    gecici = int(gecici/2)
    a += 1
print("Binary sayi:", binary)


