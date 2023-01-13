import factories_drivers.factory_driver as f_driver
from pages.base_page import BasePage
from pages.menu_page import MenuPage
from pages.search_page import SearchPage
from pages.myaccount_page import MyAccountPage 
from pages.cart_page import CartPage
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = f_driver.get_driver()

def testCase1_search():
    producto = 'Display'
    busqueda_invalida_text = 'There is no product that matches the search criteria.'
    menu_page = MenuPage(driver) 
    menu_page.buscar_producto(producto)
    search_page = SearchPage(driver)
    search_page.verificar_no_producto(busqueda_invalida_text)
    search_page.check_product_description()
    search_page.click_search()
    #menu_page.back_landingpage()
    #home_page=driver.find_element(By.XPATH,'/html/body/div[2]/ul/li[1]/a/i')
    #home_page.click()
    time.sleep(5)

    driver.save_screenshot('ScreenshotTC1_' + str(random.randint(0,101)) + '.png')


def testCase2_home():
    #menu_page = MenuPage(driver) 
    #menu_page.logo_landingpage()
    home_page=driver.find_element(By.XPATH,'/html/body/div[2]/ul/li[1]/a/i')
    home_page.click()
    driver.save_screenshot('ScreenshotTC2_' + str(random.randint(0,101)) + '.png')

    time.sleep(5)

def testCase3_register():
    firstName = 'Lupita'
    lastName = 'Aguirre'
    email = 'test2@test.com'
    telefono = '123456789'
    password = 'Password_123'
    passwordConfirm = 'Password_123'

    myaccount_page = MyAccountPage(driver)
    
    myacc_page=driver.find_element(By.XPATH,'/html/body/footer/div/div/div[4]/ul/li[1]/a')
    myacc_page.click()

    myaccount_page.click_register()
    myaccount_page.register(firstName, lastName, email, telefono, password, passwordConfirm)
    #myaccount_page.click_submit_register()
    driver.save_screenshot('ScreenshotTC3_' + str(random.randint(0,101)) + '.png')
    time.sleep(5)

    menu_page = MenuPage(driver) 
    menu_page.logo_landingpage()

    time.sleep(5)

def testCase4_login():
    usuario = 'test1@test.com'
    password = 'Password_123'


    myaccount_page = MyAccountPage(driver)
    #myaccount_page.click_myaccount()
    #myaccount_page.click_login()

    myacc_page=driver.find_element(By.XPATH,'/html/body/footer/div/div/div[4]/ul/li[1]/a')
    myacc_page.click()
    myaccount_page.login(usuario, password)
    driver.save_screenshot('ScreenshotTC4_' + str(random.randint(0,101)) + '.png')
    time.sleep(5)

def testCase5_calendar():
    menu_page = MenuPage(driver) 
    menu_page.mod_desktops()

def testCase6_review():
    menu_page = MenuPage(driver) 
    menu_page.mod_laptops()

def testCase7_module():
    menu_page = MenuPage(driver) 
    menu_page.mod_components()

def testCase9_moduleTablets():
    menu_page = MenuPage(driver) 
    menu_page.mod_tablets()

    driver.save_screenshot('ScreenshotTC9_' + str(random.randint(0,101)) + '.png')
    time.sleep(5)

def testCase10_moduleSoftware():
    menu_page = MenuPage(driver) 
    menu_page.mod_software()

    driver.save_screenshot('ScreenshotTC10_' + str(random.randint(0,101)) + '.png')
    time.sleep(5)

def testCase11_modulePhones():
    menu_page = MenuPage(driver) 
    menu_page.mod_phones()

    driver.save_screenshot('ScreenshotTC11_' + str(random.randint(0,101)) + '.png')
    time.sleep(5)


def testCase12_cart():
    cart_page = CartPage(driver)
    cart_page.add_to_cart()

    driver.save_screenshot('ScreenshotTC14_' + str(random.randint(0,101)) + '.png')
    time.sleep(5)

def testCase13_checkout():
    go_to_cart=driver.find_element(By.ID,'cart-total')
    go_to_cart.click()
    time.sleep(1)

    checkout=driver.find_element(By.XPATH,'//p[@class="text-right"]/a[2]')
    checkout.click()
        
    driver.save_screenshot('ScreenshotTC13_' + str(random.randint(0,101)) + '.png')
    time.sleep(5)

def testCase14_change_pwd():

def testCase15_logout():
#wishlist


def teardown():
    BasePage(driver).close_browser()