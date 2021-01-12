from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 
import requests 

# Information
Api_Key = ""
Ph = ""
Password = ""
Page_Link = "AstrowingMNNIT" # "Testing-103157051739885"
credits = "Credits : Image is fetched from https://apod.nasa.gov/apod/astropix.html \nThis post is made by a bot. (Amit Gupta 2nd Year CSE) \n(Source Code: https://github.com/AmitGupta7580/Facebook_Bot)"

# Fetching Image From NASA-API
api = 'https://api.nasa.gov/planetary/apod?api_key='+Api_Key
print("[+] Fetching the Json object from API")
r = requests.get(api)
image_url = r.json()['url']
description = r.json()['explanation']
title = r.json()['title']
image = requests.get(image_url)

# Saving Image
img = open("image.jpg", "wb")
img.write(image.content)
img.close()
print("[+] Image Saved")

# Opening the selenium browser
print("[+] Opening Browser")
browser = webdriver.Firefox()  

# Login to facebook
print("[+] Login into facebook")
browser.get('https://www.facebook.com/')
ph = browser.find_element_by_id('email')
ph.send_keys(Ph)                         
paswd = browser.find_element_by_id('pass')
paswd.send_keys(Password) 
login = browser.find_element_by_id('u_0_b')
login.click()
print("[+] Login Successfully")
time.sleep(3)

# navigate to page link
print("[+] Redirecting to "+Page_Link)
browser.get('https://www.facebook.com/'+Page_Link)
time.sleep(3)

# Uploading Image
print("[+] Image Uploading")
inp = browser.find_elements(By.XPATH, "//input[@type='file']")
inp[1].send_keys("F:\\AstroClub_Facebook_Autonomation\\image.jpg")
time.sleep(7)

# adding text
payload = title + '\n' + description + '\n' + credits
print("[+] Adding Description")
txt_bx = browser.find_elements(By.XPATH, "//div[@class='notranslate _5rpu' and @role='textbox']")
txt_bx[len(txt_bx)-1].send_keys(payload)
time.sleep(10)

# posting the post
print("[+] Posting ....")
post = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[4]/div/div[1]/div/span/span")
post.click()
print("[+] Post Successfully Added")

# Closing The Browser
time.sleep(5)
browser.close()