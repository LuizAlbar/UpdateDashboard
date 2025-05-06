import os
from time import sleep
from datetime import datetime
from send2trash import send2trash

# MONTH
actual_month = datetime.now().month
month = f"{actual_month:02d}"

# FILE NAME
fileRenamed = f"EvaluationReport-2025{month}.xlsx"
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

def renameReport():
    
    renamed = False
    index = 1

    while not renamed:
        try:
            for file in os.listdir(downloads_path):
                if "EvaluationReport" in file and fileRenamed not in file:
                    filePath = os.path.join(downloads_path, file)
                    newfilePath = os.path.join(downloads_path, fileRenamed)
                    
                    if os.path.exists(newfilePath):
                        send2trash(newfilePath)
                
                    os.rename(filePath, newfilePath)
                    
                    print(f"File has been renamed to {fileRenamed}")
                    renamed = True
                    break
                
        except FileNotFoundError as e:
            print("File not found")

        if not renamed:
            print(f"Waiting for file... {index}")
            
        index = index + 1
        sleep(1)
        

