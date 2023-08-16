import pyautogui
import time
import schedule
from datetime import datetime
from threading import Timer

def job_once():
    global t
    t = '20:38'
         
    while True:
    

        now = datetime.now()
        current_time = now.strftime("%H:%M")
    
        starttime = time.time()
    
        t != current_time
        print("Current Time =", current_time)
        time.sleep(5.0 - ((time.time() - starttime) % 5.0))
        
    else:    
        #pyautogui.moveTo(15, 1030, duration=0)
        time.sleep(1)
        pyautogui.click(15, 1050)
        time.sleep(1)
        pyautogui.click(15, 1000)
        time.sleep(2)
        #pyautogui.click(clicks=2, x=15, y=900)
        pyautogui.moveTo(15, 940, duration=0)
        

#schedule.every().day.at(t).do(job_once)


#def shutdown():
    ##pyautogui.moveTo(15, 1030, duration=0)
    #time.sleep(1)
    #pyautogui.click(15, 1050)
    #time.sleep(1)
    #pyautogui.click(15, 1000)
    #time.sleep(2)
    ##pyautogui.click(clicks=2, x=15, y=900)
    #pyautogui.moveTo(15, 940, duration=0)


#shutdown()
job_once()