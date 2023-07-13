
import datetime as dt
dogum=input("Doğum tarihinizi giriniz(GG.AA.YYYY):")
dogum=dt.datetime.strptime(dogum,"%d.%m.%Y")
simdi=dt.datetime.now()
fark=simdi-dogum
Yıl=fark.days//365
Ay=fark.days%365//30
Gün=fark.days%365%30
print(f"{Yıl} yıl {Ay} ay {Gün} gün yaşındasınız.")