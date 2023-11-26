liste1 = []
sayi = int(input("Total Number of List Items = "))

for i in range(1, sayi + 1):
    deger = int(input("Enter the %d List Item = "  %i))
    liste1.append(deger)

toplam = sum(liste1)
ortalama = toplam / sayi

print('\n toplam = {0} and ortalama = {1}'.format(toplam, ortalama))

print('Ortalamadan büyük elemanlar:')
for i in range(len(liste1)):
    if liste1[i] > ortalama:
        print(liste1[i], end = ' ')