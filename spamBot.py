from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import pandas as pd
from time import sleep

options = Options()
session = HTMLSession()

options.headless = True
PATH=r"C:\Users\educative\Documents\chromedriver\chromedriver.exe"

options.add_argument('headless')
driver = webdriver.Chrome()

'''
This function will insert the value "Anurodh" in the field within the form
'''
def send_name(inputElement):
    try:
        inputElement.send_keys("Anurodh")
    except:
        pass

'''
This function will insert the value "myspambot01@gmail.com" in the field within the form
'''
def send_email(inputElement):
    try:
        inputElement.send_keys("myspambot01@gmail.com")
    except:
        pass
