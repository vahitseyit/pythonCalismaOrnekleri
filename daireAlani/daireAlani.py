from cmath import pi



yariCap = float(input("Yaricapi giriniz: "))
daireAlani = pi*yariCap*yariCap
daireCevresi = 2*pi*yariCap
print("Dairenin alani {r:5.10} ".format(r=daireAlani))
print("Dairenin cevresi2 {:5.10}".format(daireCevresi))