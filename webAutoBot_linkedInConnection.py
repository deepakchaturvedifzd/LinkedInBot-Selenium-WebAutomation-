import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")
sleep(1)

username = os.environ.get("linkedInId")
password = os.environ.get("linkedInPswrd")

USERNAME = driver.find_element_by_id("session_key")
PASSWORD = driver.find_element_by_id("session_password")

USERNAME.send_keys(username)
PASSWORD.send_keys(password)
sleep(1)

signInBtn = driver.find_element_by_class_name("sign-in-form__submit-button")
signInBtn.click()
link = "https://www.linkedin.com/mynetwork/invitation-manager/"
driver.get(link)
sleep(3)
msgDropDownBtn = driver.find_element_by_xpath("/html/body/div[6]/aside/div[1]/header/section[2]/button[2]")
msgDropDownBtn.click()
acceptBtns=[]
while(len(acceptBtns)==0):
    acceptBtns=driver.find_elements_by_xpath("//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
print(len(acceptBtns))
for btn in acceptBtns:
    btn.click()
    sleep(1)

driver.close()
