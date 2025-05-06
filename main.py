from browser_util import launch_browser
from generate_report import get_report
from upload_file_mis import *
from login_verifier import *

option = 9

while option != 3:
    
    print("1) Extrair relatório \n2) Atualizar Dashboard \n3) Cancelar \n ")
    option = int(input("Opção: "))
    
    if option == 1:
        browser = launch_browser()
        launch_report(browser)
        login_required = identify_login(browser)
        
        print(login_required)
        
        if login_required:
            login(browser)
            home_loaded_verify(browser)
            launch_report(browser)
            get_report(browser)
            browser.quit()
            
        if not login_required:
            get_report(browser)
            browser.quit()
            
    elif option == 2:
        browser = launch_browser()
        open_mis(browser)
        create_file(browser)
        choose_file(browser)
        upload_file()
        subistitute_file(browser)
        browser.quit()
    
    
    elif option == 3:
        print("Até logo!")
        
    else:
        print("Opção inválida")
        
            
    
            
            
            
            
        
        
    
    
    
