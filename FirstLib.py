import time
import sys
import selenium

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def selectBrowser(browser='Chrome'):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    return driver
    
def openWeb(mainDriver, link):
    driver = mainDriver
    driver.maximize_window()
    driver.get(link)

def maximizeWeb(mainDriver):
    mainDriver.maximize_window()

def refreshPage(mainDriver):
    mainDriver.refresh()

def setDateInOut(mainDriver, dayIn, dayOut):
    checkIn = mainDriver.find_element_by_id("arrival")
    for num in range(1, 10):
        checkIn.send_keys(Keys.BACKSPACE)
    checkOut = mainDriver.find_element_by_id("departure")
    checkOut.clear()
    time.sleep(1)
    checkOut.send_keys(dayOut)
    time.sleep(1)
    checkIn.send_keys(dayIn)

def findWithLinkTextAndClick(mainDriver, str):
    elementFound = mainDriver.find_element_by_link_text(str)
    elementFound.click()

def findWithCSSAndClick(mainDriver, css):
    elementFound = mainDriver.find_element_by_css_selector(css)
    elementFound.click()

def findWithXPathAndClick(mainDriver, xPathStr):
    elementFound = mainDriver.find_element_by_xpath(xPathStr)
    elementFound.click()

def findWithIDAndClick(mainDriver, id):
    elementFound = mainDriver.find_element_by_id(id)
    elementFound.click()

def findWithIDAndSendKey(mainDriver, id, str):
    elementFound = mainDriver.find_element_by_id(id)
    elementFound.clear()
    elementFound.send_keys(str)

def findWithXPathAndSendKey(mainDriver, xPathStr, str):
    elementFound = mainDriver.find_element_by_xpath(xPathStr)
    elementFound.send_keys(str)

def findWithXPathAndSelectByIndex(mainDriver, xPathStr, index):
    select = Select(mainDriver.find_element_by_xpath(xPathStr))
    select.select_by_index(index)
    
def mySleep(sec):
    print "Sleep %d" % sec
    time.sleep(sec)
    print "End Sleep %d" % sec

def test1():
    driver = self.driver
    driver.maximize_window()
    driver.get("https://dev.omenahotels.com/en/booking/")

    self.mySleep(3)
    chooseHotel = driver.find_element_by_xpath("//button[@type='button']")
    chooseHotel.click()
    driver.find_element_by_xpath("//div[@id='search']/div/div/div/div/div/div/div/ul/li[10]/a/span").click()
    self.mySleep(1)
    checkIn = driver.find_element_by_id("arrival")
    checkIn.clear()
    checkIn.send_keys("11.4.2017")
    self.mySleep(1)
    checkOut = driver.find_element_by_id("departure")
    checkOut.clear()
    self.mySleep(1)
    checkOut.send_keys("15.4.2017")       
    self.mySleep(1)
    checkIn = driver.find_element_by_id("add-room-1")
    checkIn.click()
    self.mySleep(1)
    checkIn = driver.find_element_by_id("continue")
    checkIn.click()
            
    self.mySleep(3)
    driver.find_element_by_id("first-name").send_keys("Green")
    self.mySleep(1)
    driver.find_element_by_id("last-name").send_keys("Dark")
    self.mySleep(1)
    driver.find_element_by_id("email").send_keys("darkgreener@colors.com")
    self.mySleep(1)
    driver.find_element_by_id("confirm-email").send_keys("darkgreener@colors.com")
    self.mySleep(1)
    mobileCountry = driver.find_element_by_xpath("//button[@type='button']")
    mobileCountry.click()
    mobileCountryValue = driver.find_element_by_link_text("Finland +358").click()
    self.mySleep(1)
    driver.find_element_by_id("mobile").send_keys("342350888")
    self.mySleep(1)
    driver.find_element_by_id("address").send_keys("113 Grand avenue")
    self.mySleep(1)
    driver.find_element_by_id("postal-code").send_keys("113")
    self.mySleep(1)
    driver.find_element_by_id("city").send_keys("Sunset")
    self.mySleep(1)
    country = driver.find_element_by_xpath("//button[@class='btn dropdown-toggle btn-default' and @data-id='country']")
    country.click()
    country = driver.find_element_by_link_text("Sweden").click()
    self.mySleep(1)
    driver.find_element_by_id("company").send_keys("ATM Inc")
    self.mySleep(1)
    driver.find_element_by_id("reference").send_keys("To be filled")
    self.mySleep(1)
    driver.find_element_by_id("accept-terms").click()
    self.mySleep(1)
    driver.find_element_by_css_selector("input.method.type-b").click()
    self.mySleep(14)

    name = driver.find_element_by_xpath("//input[@class='login' and @name='id']")
    name.send_keys("123456")
    self.mySleep(1)
    passw = driver.find_element_by_xpath("//input[@class='login' and @name='pw']")
    passw.send_keys("7890")
    driver.find_element_by_xpath("//input[@class='Nappi' and @name='ktunn']").click()
    self.mySleep(3)
    
    key = driver.find_element_by_xpath("//input[@name='avainluku']")
    key.send_keys("1111")
    driver.find_element_by_xpath("//input[@class='Nappi' and @name='avainl']").click()
    self.mySleep(3)
    
    driver.find_element_by_xpath("//input [@id='Toiminto']").click()
    self.mySleep(15)
    
    key = driver.find_element_by_xpath("//input[@name='personal-id']")
    key.send_keys("111113-113Y")
    purposeVisit = Select(driver.find_element_by_xpath("//select[@class='form-control purpose-of-visit validation-check' and @name='purpose-of-visit']"))
    purposeVisit.select_by_index(2)
    driver.find_element_by_xpath("//button[@class='btn btn-red btn-full-width save-guest']").click()
    self.mySleep(3)
    driver.find_element_by_xpath("//button[@id='add-guest-1']").click()
    self.mySleep(5)
    
    driver.find_element_by_xpath("//input[@class='form-control first-name validation-check' and @value='']").send_keys("Blue")
    self.mySleep(1)
    driver.find_element_by_xpath("//input[@class='form-control last-name validation-check' and @value='']").send_keys("Light")
    self.mySleep(1)
    driver.find_element_by_xpath("//input[@class='form-control personal-id validation-check' and @value='']").send_keys("121113-113L")
    self.mySleep(1)
    purposeVisit = Select(driver.find_element_by_xpath("(//select[@class='form-control purpose-of-visit validation-check' and @name='purpose-of-visit'])[2]"))
    purposeVisit.select_by_index(2)
    self.mySleep(1)
    driver.find_element_by_xpath("//input[@class='form-control mobile validation-check' and @value='']").send_keys("+358234567113")
    self.mySleep(1)
    driver.find_element_by_xpath("//input[@class='form-control email validation-check' and @value='']").send_keys("mail2@x.com")
    self.mySleep(1)
    driver.find_element_by_xpath("(//button[@class='btn btn-red btn-full-width save-guest'])[2]").click()
    self.mySleep(3)
    driver.find_element_by_xpath("//button[@id='booking-confirm']").click()
    self.mySleep(5)
    driver.find_element_by_xpath("//a[@class='btn btn-red btn-full-width']").click()
    