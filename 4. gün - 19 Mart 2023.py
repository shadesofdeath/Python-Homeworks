from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())


# Ödev 1 : Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

class start_test:
    def KontrolEt1(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        parola_kontrol = driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_sonuc = parola_kontrol.text == "Epic sadface: Username is required"
        print(f"Testin Sonucu : {test_sonuc}")

# -----------------------------------------------------------------------------------#
# Ödev 2 : Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

    def KontrolEt2(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        username_kontrol = driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_sonuc = username_kontrol.text == "Epic sadface: Password is required"
        print(f"Testin Sonucu : {test_sonuc}")

# #-----------------------------------------------------------------------------------#
# Ödev 3 : Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

    def KontrolEt3(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        username_login = driver.find_element(By.ID, "user-name")
        username_login.send_keys("locked_out_user")
        password_login = driver.find_element(By.ID, "password")
        password_login.send_keys("secret_sauce")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        cıktı_kontrol = driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_sonuc = cıktı_kontrol.text == "Epic sadface: Sorry, this user has been locked out"
        print(f"Test Sonucu : {test_sonuc} ")

# -----------------------------------------------------------------------------------#
# Ödev 4 : Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
# Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)

    def KontrolEt4(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        sleep(2)
        if driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button"):
            print("Çarpı Butonu Çıktığı Tespit Edildi!")
            kapat = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
            kapat.click()
            print("Çarpı Butonu Kapatıldı")
        else:
            print("Çarpı butonu tespit edilemedi.")

# -----------------------------------------------------------------------------------#
# Ödev 5 : Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.

    def KontrolEt5(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(3)
        username = driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        sleep(2)
        password = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
        password.send_keys("secret_sauce")
        sleep(2)
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()

# -----------------------------------------------------------------------------------#
# Ödev 6 : Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

    def KontrolEt6(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        username = driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        password = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
        password.send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        ürün_adet = driver.find_element(By.CLASS_NAME, "inventory_list")
        sleep(3)
        print(f"ÜRÜN ADETİ : {len(ürün_adet)}")
        product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
        sleep(3)
        print(f"ÜRÜN ADETİ : {len(product_elements)}")


start_test().KontrolEt1()
start_test().KontrolEt2()
start_test().KontrolEt3()
start_test().KontrolEt4()
start_test().KontrolEt5()
start_test().KontrolEt6()

# -----------------------------------------------------------------------------------#
