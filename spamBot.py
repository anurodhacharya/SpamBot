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

def findElements(url):
    driver.get(url)
    allForms = retrieve_forms(url)
    for i, singleForm in enumerate(allForms, 1):
        
        # Finding the input tag within the form
        for input in singleForm.find_all("input"):
            pathInput = str(find_xpath(input))        
            
            # We find the input element within the form using it's XPath
            elementInput = driver.find_element(By.XPATH, pathInput)
            
            # We find the name,id and type field and extract each of those values in lowercase
            nameField = elementInput.get_attribute('name')     
            # forField = elementInput.get_attribute('for')     
            idField = elementInput.get_attribute('id') 
            # classField = elementInput.get_attribute('class')    
            typeField = elementInput.get_attribute('type')         
                
            # Different keywords that could indicate email field
            patternEmail = "email EMAIL mail e-mail MAIL E-mail"        

            # We send the fields for checking if those name,id and type field have required values that we are looking for
            processing(nameField, idField, typeField, patternEmail, elementInput, isMailSubmit=True)
    
            patternName = "name fname lname firstname lastname Fname Lname"   
            processing(nameField, idField, typeField, patternName, elementInput, isNameSubmit=True)                               

            patternPhone = "phone mobile pno number contact mob"       
            processing(nameField, idField, typeField, patternPhone, elementInput, isPhoneSubmit=True)                                       

            patternSubmit = "submit SUBMIT Submit register Register subscribe SUBSCRIBE"  
            processing(nameField, idField, typeField, patternSubmit, elementInput, isSubmit=True)  