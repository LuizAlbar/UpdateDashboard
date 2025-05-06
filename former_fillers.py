from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from file_renamer import renameReport

# DAY
actual_day =  datetime.now().day
actual_day = actual_day - 1
day = f"{actual_day:02d}"

# MONTH
actual_month = datetime.now().month
month = f"{actual_month:02d}"

def initial_date(browser):
    
    wait = WebDriverWait(browser, 20)
    xpath = "/html/body/app-root/div/main/app-evaluation-report/div/article/main/div[1]/div[1]/div/app-input[1]/section/input"
    btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    btn.send_keys(f"01/{month}/2025")
     
def final_date(browser):
    
    wait = WebDriverWait(browser, 20)
    xpath = "/html/body/app-root/div/main/app-evaluation-report/div/article/main/div[1]/div[1]/div/app-input[2]/section/input"
    btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    btn.send_keys(f"{day}/{month}/2025")
   
    
def all_checkboxes(browser):
    
    wait = WebDriverWait(browser, 30)
    xpaths = [
        "/html/body/app-root/div/main/app-evaluation-report/div/article/main/div[1]/div[1]/app-select[1]/div/div[2]/div[2]/div[1]/app-check-box/div/div",
        '/html/body/app-root/div/main/app-evaluation-report/div/article/main/div[1]/div[1]/app-select[2]/div/div[2]/div[2]/div[1]/app-check-box/div/div',
        '/html/body/app-root/div/main/app-evaluation-report/div/article/main/div[1]/div[2]/app-select[1]/div/div[2]/div/div[1]/app-check-box/div/div',
        '/html/body/app-root/div/main/app-evaluation-report/div/article/main/div[1]/div[2]/app-select[2]/div/div[2]/div[2]/div[1]/app-check-box/div/div' 
        
    ]

    divs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "input-icon")))
    
    
    for index, div in enumerate(divs):
        ActionChains(browser).move_to_element(div).click().perform()
        
        if index < len(xpaths):
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths[index])))
            checkbox.click()
            print(f"Checkbox {index + 1} clicked")
        
    generate(browser)
    renameReport()

def generate(browser):
    
    wait = WebDriverWait(browser, 20)
    xpath = "/html/body/app-root/div/main/app-evaluation-report/div/article/main/div[2]/app-primary-button/button"
    btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    btn.click()
        

