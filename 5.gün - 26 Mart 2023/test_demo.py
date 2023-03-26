import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'
PRODUCT_NAME = 'Sauce Labs Backpack'

LOGIN_INPUT = (By.ID, 'user-name')
PASSWORD_INPUT = (By.ID, 'password')
LOGIN_BUTTON = (By.ID, 'login-button')
PRODUCT_LABEL = (By.XPATH, f"//div[text()='{PRODUCT_NAME}']")
ADD_TO_CART_BUTTON = (By.XPATH, f"//div[text()='{PRODUCT_NAME}']/following::button")
CART_BUTTON = (By.XPATH, "//a[@class='shopping_cart_link']")
CART_ITEM_LABEL = (By.XPATH, f"//div[text()='{PRODUCT_NAME}']")

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()

def test_login(driver):
    login_input = driver.find_element(*LOGIN_INPUT)
    login_input.send_keys(USERNAME)
    password_input = driver.find_element(*PASSWORD_INPUT)
    password_input.send_keys(PASSWORD)
    login_button = driver.find_element(*LOGIN_BUTTON)
    login_button.click()
    product_label = driver.find_element(*PRODUCT_LABEL)
    assert product_label.is_displayed()
    driver.save_screenshot('test_login.png')

def test_add_to_cart(driver):
    test_login(driver)
    add_to_cart_button = driver.find_element(*ADD_TO_CART_BUTTON)
    add_to_cart_button.click()
    cart_button = driver.find_element(*CART_BUTTON)
    cart_button.click()
    cart_item_label = driver.find_element(*CART_ITEM_LABEL)
    assert cart_item_label.is_displayed()
    driver.save_screenshot('test_add_to_cart.png')

def test_logout(driver):
    test_login(driver)
    account_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    account_button.click()
    sleep(3)
    logout_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]')
    logout_button.click()
    assert driver.current_url == 'https://www.saucedemo.com/'

def test_cart(driver):
    test_add_to_cart(driver)
    cart_button = driver.find_element(*CART_BUTTON)
    cart_button.click()
    cart_item_label = driver.find_element(*CART_ITEM_LABEL)
    assert cart_item_label.is_displayed()
    driver.save_screenshot('test_cart.png')
