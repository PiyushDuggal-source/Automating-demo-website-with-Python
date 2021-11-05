import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver


class Automation(webdriver.Chrome):
    def __init__(self, exiting=True):
        self.ex = exiting

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(options=options)

        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.ex:
            self.quit()

    def get_website(self):
        self.get('http://tutorialsninja.com/demo/')

    def select_phones_and_quantity(self, count=1):
        phones_section = self.find_element_by_xpath('//a[text()="Phones & PDAs"]')
        phones_section.click()

        select_iphone = self.find_element_by_xpath('//a[text()="iPhone"]')
        select_iphone.click()

        quantity = self.find_element_by_id('input-quantity')
        quantity.clear()
        quantity.send_keys(count)

    def take_screenshot_of_last_pic(self):
        get_img = self.find_element_by_xpath('//ul[@class="thumbnails"]/li[last()]')
        get_img.click()
        time.sleep(2)
        self.save_screenshot('screenshot' + str(random.randint(0, 101)) + '.png')
        close_btn = self.find_element_by_xpath("//button[@title='Close (Esc)']")
        close_btn.click()

    def add_to_cart(self):
        atc_btn = self.find_element_by_id('button-cart')
        atc_btn.click()

    def select_laptop_and_quantity(self, count=1):
        laptop_section = self.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
        laptop_section.click()
        # action = ActionChains(self)
        # action.move_to_element(laptop_section).perform()
        select_laptop_section = self.find_element_by_xpath('//a[text()="Show All Laptops & Notebooks"]')
        select_laptop_section.click()
        select_laptop = self.find_element_by_xpath('//a[text()="MacBook Air"]')
        select_laptop.click()
        quantity = self.find_element_by_id('input-quantity')
        quantity.clear()
        quantity.send_keys(count)

    def go_to_cart(self):
        cart_btn = self.find_element_by_id('cart-total')
        cart_btn.click()

        checkout_btn = self.find_element_by_xpath('//*[@id="cart"]/ul/li[2]/div/p/a[2]/strong/i')
        checkout_btn.click()

    def testing(self, number):
        cart_btn = self.find_element_by_xpath('//*[@id="cart"]/button')
        cart_btn.click()
        check = self.find_element_by_xpath('//*[@id="cart"]/ul/li[1]/table/tbody/tr/td[3]').text.strip()

        if check == ('x ' + str(number)):
            print('Every Thing is OK!')
        else:
            print('not ok!')

        cart_btn.click()

    def checking_out(self, fname=None, lname=None, email=None, tele=None, companyName=None, address=None,
                     city=None, pcode=None):
        guest_checkout_btn = self.find_element_by_xpath(
            '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
        guest_checkout_btn.click()

        continue_btn = self.find_element_by_xpath('//*[@id="button-account"]')
        continue_btn.click()

        time.sleep(2)
        # First Name
        self.find_element_by_id('input-payment-firstname').send_keys(fname)
        # Last Name
        self.find_element_by_id('input-payment-lastname').send_keys(lname)
        # Email
        self.find_element_by_id('input-payment-email').send_keys(email)
        # Telephone
        self.find_element_by_id('input-payment-telephone').send_keys(tele)
        # CompanyName
        self.find_element_by_id('input-payment-company').send_keys(companyName)
        # Address
        self.find_element_by_id('input-payment-address-1').send_keys(address)
        # City
        self.find_element_by_id('input-payment-city').send_keys(city)
        # Post Code
        self.find_element_by_id('input-payment-postcode').send_keys(pcode)
        # Country
        country = self.find_element_by_id('input-payment-country')
        # zone
        region = self.find_element_by_id('input-payment-zone')

        dropdown_c = Select(country)
        time.sleep(1)
        dropdown_c.select_by_index(106)
        time.sleep(1)
        dropdown_r = Select(region)
        dropdown_r.select_by_index(9)