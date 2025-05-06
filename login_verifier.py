from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_util import *

def identify_login(browser):
    # True or False
    try:
        xpath = "/html/body/app-root/div/main/app-login/div/div/div[2]/app-login-button"
        wait = WebDriverWait(browser, 3)
        btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        btn.click()
        print('Login screen detected')
        return True

    except:
        print('No login required')
        return False
    
  
    
def login(browser):
    
    xpath = '//*[@id="tilesHolder"]/div[1]/div'
    wait = WebDriverWait(browser, 20)
    btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    btn.click()

def launch_report(browser):
    
    url = ""
    browser.get(url)
    print('Report screen launched')
    
def home_loaded_verify(browser):
    # True or False
    try:
        xpath = '/html/body/app-root/div/app-navbar/nav/div[1]/img'
        wait = WebDriverWait(browser, 25)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        
        return True
    
    except:
        print("Home page couldn't be loaded")
        return False
        
    



