import time
from datetime import datetime
import os


def shutdown():
    a = int(input("Choose if you want to: 1 - shutdown, 2 - restart: "))
    user_hour = int(input("Provide hour: "))
    user_minute = int(input("Provide minute: "))

    while True:
        now = datetime.now()
        starttime = time.time()
        current_time = now.strftime("%H:%M")

        # print("Current Time =", current_time)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

        if now.hour == user_hour and now.minute == user_minute:
            print("pora na ceesa")
            time.sleep(1)
            if a == 1:
                os.system("shutdown /s /t 1")  # shutdown
            elif a == 2:
                os.system("shutdown /r /t 1")  # restart
            break


shutdown()
