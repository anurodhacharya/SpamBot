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

'''
This function will insert the value "123-456-7890" in the field within the form
'''
def send_contact(inputElement):
    try:
        inputElement.send_keys("123-456-7890")
    except:
        pass    

'''
This function will submit all the values within the form
'''
def submit(inputElement):
    try:
        inputElement.click()
    except:
        pass

'''
This function will retrieve all the forms that are present within a webpage.
'''
def retrieve_forms(url):
    res = session.get(url)
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

'''
This function will retrieve the xpath value of the element that it has been passed with.
'''
def find_xpath(tag):
    items = []
    present = tag if tag.name else tag.parent
    while present.parent:
        siblings = present.parent.find_all(present.name, recursive=False)
        index = siblings.index(present) + 1 if len(siblings) > 1 else None
        items.append(f"{present.name}{f'[{index}]' if index else ''}")
        present = present.parent
    items.reverse()
    return '/'.join(items)

'''
This function is responsible for checking if the value in the element field of the website matches with our required values.
'''
def processing(name, id, type, regex, inputElement, isMailSubmit=False, isNameSubmit=False, isPhoneSubmit=False, isSubmit=False):
    ctr = 0
    items = regex.split(" ")
    for word in items:
        if name == word:
            ctr+=1
    for word in items:
        if id == word:
            ctr+=1
    for word in items:
        if type == word:
            ctr+=1
    
    if ctr >= 1 and isMailSubmit == True:
        send_email(inputElement)
    if ctr >= 1 and isNameSubmit == True:
        send_name(inputElement)
    if ctr >= 1 and isPhoneSubmit == True:
        send_contact(inputElement)
    if isSubmit == True:
        submit(inputElement)
