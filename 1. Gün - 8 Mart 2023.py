# Python programlama dilinde kullanılan veri tipleri şunlardır:

# Sayılar (Numbers): Sayılar iki ana kategoriye ayrılır: tam sayılar (integers) ve ondalık sayılar (floats). Tam sayılar bir virgülden önceki herhangi bir sayıdır, örneğin: 2, 3, 4, 1000. Ondalık sayılar ise virgülden sonra en az bir sayı içerir, örneğin: 2.0, 3.14, 0.25.

# Dizeler (Strings): Dizeler, karakterlerin bir araya gelmesiyle oluşan metinsel verilerdir. Örneğin: "Merhaba", "Python".

# Listeler (Lists): Listeler, bir araya getirilmiş verilerin bir koleksiyonudur. Listeler içinde farklı veri tipleri bulunabilir. Örneğin: [1, 2, 3], ["merhaba", "dünya"], [1, "iki", 3.0].

# Demetler (Tuples): Demetler, bir araya getirilmiş verilerin bir koleksiyonudur. Ancak, listelerden farklı olarak, demetler değiştirilemez (immutable) veri tipleridir. Örneğin: (1, 2, 3), ("merhaba", "dünya"), (1, "iki", 3.0).

# Sözlükler (Dictionaries): Sözlükler, anahtar-değer çiftleri şeklinde verileri saklarlar. Anahtarlar genellikle bir dize (string) şeklinde kullanılır ve değerler değişebilir (mutable) veri tipleri olabilir. Örneğin: {"isim": "Ahmet", "yaş": 25, "sevdiği_renkler": ["mavi", "yeşil"]}.

# Kümeler (Sets): Kümeler, benzersiz elemanları içeren veri tipleridir. Kümelerdeki elemanlar değiştirilebilir (mutable) veri tipleri olabilir. Örneğin: {1, 2, 3}, {"merhaba", "dünya"}.


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