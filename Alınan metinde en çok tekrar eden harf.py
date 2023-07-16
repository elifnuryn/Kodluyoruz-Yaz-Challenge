def en_cok_tekrar_eden_harf(metin):
    harf_sayilari = {}
    for harf in metin:
        if harf.isalpha():
            harf = harf.lower()
            if harf in harf_sayilari:
                harf_sayilari[harf] += 1
            else:
                harf_sayilari[harf] = 1

    en_cok_tekrar_eden_harf = None
    en_cok_tekrar_sayisi = 0

    for harf, sayi in harf_sayilari.items():
        if sayi > en_cok_tekrar_sayisi:
            en_cok_tekrar_eden_harf = harf
            en_cok_tekrar_sayisi = sayi

    return en_cok_tekrar_eden_harf, en_cok_tekrar_sayisi


metin = input("Lütfen bir metin giriniz: ")
en_cok_tekrar_eden_harf, tekrar_sayisi = en_cok_tekrar_eden_harf(metin)

print("Girilen metinde en çok tekrar eden harf: ", en_cok_tekrar_eden_harf)
print("Tekrar sayısı: ", tekrar_sayisi)