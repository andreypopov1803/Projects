from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')
 
# login_link = browser.find_element(By.LINK_TEXT,"//a[text()='Log in']")
# login_link.click()
sleep(2)
 
username_input = browser.find_element(By.CSS_SELECTOR,"input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']")
username_input.send_keys("andrey.bat.96")
password_input.send_keys("Popovav1803_")
# login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button = browser.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()
sleep(30)
browser.close()

# last = test.find_element_by_xpath('//*[@id="mG61Hd"]
# last = test.find_element("xpath", '//*[@id="mG61Hd"]