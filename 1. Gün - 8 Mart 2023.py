# Değişken olarak örnek vermek gerekirse kodlama.io sitesinde kursların kategorilere ayrıldığı
# bölümlerde hepsinde "Ücretsiz" yazısı yazıyor buradaki ücretsiz yazısı bir yerde tanımlanmış
# bir değişken olabilir.
# Kodlama.io sitesi değişken örneği ;
price = "Ücretsiz"
print(price)

# Şart bloklarına örnek verecek olursam mesela siteye giriş yapma bölümü olabilir
# database de bulunan username ve pass değerleri kullanıcının girdiği ile karşılaştırılır
# doğru ise kullanıcı siteye giriş yapar yanlış girerse hata mesajı döndürülebilir.
# Kodlama.io sitesi şart bloğu örneği ;
username = "user"
password = "123456"

loginUsername = input("Kullanıcı adı veya e posta giriniz : ")
loginPassword = input("Parolanızı giriniz : ")

if loginUsername == username:
    if loginPassword == password:
        print("Kullanıcı adı ve şifre doğru, ana sayfaya yönlendiriliyorsunuz...")
    else:
        print("Parolanız yanlış!")
else:
    print("Kullanıcı adınız yanlış!")