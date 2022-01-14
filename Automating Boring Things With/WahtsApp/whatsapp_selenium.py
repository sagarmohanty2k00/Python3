import numbers
from selenium import webdriver as web

driver = web.Chrome('/Users/rauna/Downloads/chromedriver')

driver.get('https://web.whatsapp.com/')

number = '+919938850417'
message = "mama tu gote ..."
