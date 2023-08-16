import pyautogui
import time
import schedule

#def job_once():
#    #pyautogui.moveTo(15, 1030, duration=0)
#    #time.sleep(1)
#    pyautogui.click(15, 1030)
#    time.sleep(1)
#    pyautogui.click(15, 980)
#    time.sleep(2)
#    pyautogui.click(clicks=2, x=15, y=900)
#    #pyautogui.moveTo(15, 900, duration=0)
#    return schedule.CancelJob
#
#schedule.every().day.at('15:30').do(job_once)


def shutdown():
    #pyautogui.moveTo(15, 1030, duration=0)
    time.sleep(1)
    pyautogui.click(15, 1050)
    time.sleep(1)
    pyautogui.click(15, 980)
    time.sleep(2)
    #pyautogui.click(clicks=2, x=15, y=900)
    pyautogui.moveTo(15, 900, duration=0)


shutdown()