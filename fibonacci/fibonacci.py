i=0
ilk_deger = 1
ikinci_deger = 1
print(ilk_deger)
print(ikinci_deger)
while(i<50):
    sonraki = ilk_deger + ikinci_deger
    ilk_deger = ikinci_deger
    ikinci_deger = sonraki
    print(sonraki)
    i = i+1