# -*- coding: ISO-8859-1
import time
import unittest
import sys
import selenium

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test(unittest.TestCase):
    def setUp(self, logname="log.txt"):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        sys.terminal = sys.stdout
        sys.log = open(logname, 'w')
        #sys.stdout = Logger(logname)
        
    def mySleep(self, sec):
        print "Sleep %d" % sec
        time.sleep(sec)
        print "End Sleep %d" % sec
    
    def test1(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://dev.omenahotels.com/en/booking/")
        self.mySleep(3)

        chooseHotel = driver.find_element_by_xpath("//button[@type='button']")
        chooseHotel.click()
        driver.find_element_by_xpath("//div[@id='search']/div/div/div/div/div/div/div/ul/li[10]/a/span").click()
        self.mySleep(1)	
        checkIn = driver.find_element_by_id("arrival")
        for num in range(1, 10):
            checkIn.send_keys(Keys.BACKSPACE)
        checkOut = driver.find_element_by_id("departure")
        checkOut.clear()
        self.mySleep(3)
        checkOut.send_keys("15.4.2017")
        self.mySleep(3)
        checkIn.send_keys("11.4.2017")
        self.mySleep(3)
        chooseHotel = driver.find_element_by_xpath("//button[@type='button']")
        chooseHotel.click()
        driver.find_element_by_xpath("//div[@id='search']/div/div/div/div/div/div/div/ul/li[9]/a/span").click()
        self.mySleep(2)
        checkIn = driver.find_element_by_xpath("//button[@id='add-room-1']")
        checkIn.click()
        self.mySleep(2)
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
        
        
        
    def tearDown(self):
        self.mySleep(1)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()