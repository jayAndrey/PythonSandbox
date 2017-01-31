import webbrowser
import time

count = 0
while count < 3:
    time.sleep(20)
    webbrowser.open("http://tut.by")
    count += 1


