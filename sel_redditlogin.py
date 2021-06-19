from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

username = input("Username: ")
#password = input("Password: ")
password = getpass()

driver.get('https://www.reddit.com/')

time.sleep(2)

loginbtn = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a[1]')
loginbtn.click()

time.sleep(2)

frame = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div[2]/div/iframe')
driver.switch_to.frame(frame)

uname = driver.find_element_by_id("loginUsername")
uname.click()
uname.send_keys(username)

time.sleep(1)

passw = driver.find_element_by_id("loginPassword")
passw.click()
passw.send_keys(password)

time.sleep(1)

passw.send_keys(Keys.ENTER)

#submitbtn = driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button')
#submitbtn.click()

print('Login successful!')


