from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from browser_util import *

import pyautogui as pag

def create_file(browser): 
    xpath = '//*[@id="appRoot"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/button/span'
    wait = WebDriverWait(browser, 20)
    btn =  wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    btn.click()

def choose_file(browser):
    sleep(1)
    xpath = '//*[@id="id__78-menu"]/div/ul/li[1]/button/div/span'
    wait = WebDriverWait(browser, 20)
    btn =  wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    btn.click()

def upload_file():
    sleep(2)
    pag.write("EvaluationReport-202504.xlsx")
    pag.press('enter')


def subistitute_file(browser):
    xpath = "/html/body/div[11]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/button/span"
    wait = WebDriverWait(browser, 20)
    btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    btn.click()
    sleep(5)

def open_mis(browser):
    
    url = ''
    browser.get(url)