from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.instagram.com/")

browser.implicitly_wait(10)
# Finds user field and inputs the username
userElem = browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")
userElem.send_keys("********") #Insert Username Here

# Finds the password field and input the password
passElem = browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input")
passElem.send_keys("********") #Insert Password Here

# Find and click the login button
buttonElem = browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button")
buttonElem.click()

# When message to turn on notifications comes on "Not Now" will be clicked
notElem = browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm")
notElem.click()