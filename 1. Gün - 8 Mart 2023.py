# Kodlama.io sitesi değişken örneği ;
price = "Ücretsiz"
print(price)

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