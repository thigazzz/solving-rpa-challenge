import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.rpachallenge.com'

form_values = pd.read_excel('./material/challenge.xlsx')
number_of_rounds = 10

browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get(url)

start_challenge_button_element = browser.find_element(By.XPATH, "//*[text()='Start']")
start_challenge_button_element.click()

def populate_input_element(label_element, head_name, round_index):
    input_element = browser.find_element(By.CSS_SELECTOR, f"input[ng-reflect-name='label{label_element}']")
    input_element.send_keys(str(form_values[head_name][round_index]))

for round_index in range(number_of_rounds):
    populate_input_element('FirstName', 'First Name', round_index)
    populate_input_element('Address', 'Address', round_index)
    populate_input_element('Phone', 'Phone Number', round_index)
    populate_input_element('LastName', 'Last Name ', round_index)
    populate_input_element('Role', 'Role in Company', round_index)
    populate_input_element('CompanyName', 'Company Name', round_index)
    populate_input_element('Email', 'Email', round_index)

    browser.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()


time.sleep(2)
browser.close()
