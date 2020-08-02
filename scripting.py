from selenium import webdriver
browser = webdriver.Firefox(executable_path="C:\\Users\\Tincy\\geckodriver-v0.27.0-win64\\geckodriver.exe")
browser.get("https://www.facebook.com")
username = browser.find_element_by_id("email")   #find_element_by_id is to find required element
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("me@gmail.com")  #send_keys to send data into box
password.send_keys("mypassword")
submit.click()
