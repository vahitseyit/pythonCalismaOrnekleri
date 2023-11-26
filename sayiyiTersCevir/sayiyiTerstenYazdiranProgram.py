sayi = int(input("Tersten yazilmasini istedigiiniz sayiyi girin"))
ters = 0
while(sayi > 0):
    gecici = sayi %10
    ters = (ters *10) + gecici
    sayi = int(sayi / 10)
print("\n Sayinin ters cevirilmis hali=", ters)

# %%
class employee():
    pass
