def karhesabı(maliyet, satış_fiyatı):
    if maliyet >= satış_fiyatı:
        print("Maliyet satış fiyatından büyük veya eşit olduğundan kar edilememektedir.")
    else:
        satışadedi = 1
        kar = satış_fiyatı - maliyet

        while kar > 0:
            print(f"{satışadedi} adet ürün satıldığında kar edilmeye başlanır.")
            satışadedi += 1
            kar = satış_fiyatı * satışadedi - maliyet * satışadedi
            break

        
# Değişken değerleri
maliyet = 117.73
satış_fiyatı = 174.99

# Kar hesabı
karhesabı(maliyet, satış_fiyatı)
