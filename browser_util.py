from selenium import webdriver


def launch_browser():
    
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    user_data_dir = "C:\\Users\\lgbarbosa1\\AppData\\Local\\Google\\Chrome\\User Data"
    
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    options.add_experimental_option("detach", True)
    options.add_argument(f"user-data-dir={user_data_dir}")
    
    browser = webdriver.Chrome(options=options)
    return browser

    
    

    