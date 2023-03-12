                    ### 2 GÜN ÖDEVLERİ ###
#--------------------------------------------------------------#
# 1. Ödev

ogrenciler = []

ogrenciAdiSoyadi = str(input("Öğrencinin Adını ve Soyadını giriniz: "))

ogrenciler.append(ogrenciAdiSoyadi)
print(f"Öğrencinin Adı ve soyadı : {ogrenciAdiSoyadi}")

#--------------------------------------------------------------#
# 2. Ödev
ogrenciler = ["Berkay AY","Alev AY"]

ogrenciAdiSoyadi = input("Öğrencinin adını ve soyadını giriniz: ")

for ogrenci in ogrenciler:
    if ogrenciAdiSoyadi == ogrenci:
        ogrenciler.remove(ogrenci)
        print(f"{ogrenciAdiSoyadi} öğrencisi listeden silindi!")
        break
else:
    print(f"{ogrenciAdiSoyadi} isimli öğrenci listede bulunamadı.")

print(f"Güncel liste şu şekildedir: {ogrenciler}")

#--------------------------------------------------------------#
# 3. Ödev

ogrenciler = []

i = 0
ogrenciAdet = int(input("Kaç Öğrenci eklemek istersini ?: "))

while i < ogrenciAdet:
    ogrenciAdiSoyadi = input("Öğrencinin adını ve soyadını giriniz: ")
    ogrenciler.append(ogrenciAdiSoyadi)
    i += 1
print(ogrenciler)

#--------------------------------------------------------------#
# 4. Ödev

ogrenciler = ["Berkay AY","Alev AY"]

for ogrenci in ogrenciler:
    print(ogrenci)

#--------------------------------------------------------------#
# 5. Ödev

ogrenciler = ["Berkay AY", "Alev AY", "User1", "User2"]

ogrenciAdi = str(input("Öğrenci adı giriniz: "))

ogrenci_numarasi = ogrenciler.index(ogrenciAdi) + 1

print("Öğrenci numarası:", ogrenci_numarasi)

#--------------------------------------------------------------#
# 5. Ödev

ogrenciler = ["Berkay AY", "Alev AY", "User1", "User2"]

sor = int(input("Kaç adet öğrenci sileceksiniz ?: "))

i = 0

while i < sor:
    ogernciSil = str(input("Silmek istediğiniz öğrencinin adını ve soadını girin : "))
    ogrenciler.remove(ogernciSil)
    i += 1
print(f"Liste güncel hali : {ogrenciler}")

#--------------------------------------------------------------#