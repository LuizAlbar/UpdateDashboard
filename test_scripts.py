from login_verifier import *
from browser_util import *
from generate_report import *
from time import sleep

browser = launch_browser()

launch_report(browser)
identify_login(browser)
login(browser)
sleep(5)
launch_report(browser)
sleep(1)

get_report(browser)

print(identify_login(browser))

sleep(25)
browser.quit()

