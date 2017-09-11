from mss import mss
import keyboard
import ftplib
import time
import os

sct = mss()
ftp = ftplib.FTP()

ftp_username = "USERNAME"
ftp_password = "PASSWORD"
ftp_host = "WEBSITE.COM"
ftp_dir = "/PATH/TO/FOLDER"
ftp_port = "21"

def handle_keys():
    name = time.strftime("%d-%m-%Y %H-%M-%S") + " screenshot.png"
    path = os.getenv('LOCALAPPDATA') + "\\Temp\\" + name
    
    sct.shot(mon=-1, output=path)
    
    print("Connecting to FTP")
    ftp.connect(ftp_host, ftp_port)
    print("Connected")
    
    try:
        ftp.login(ftp_username, ftp_password)
        ftp.cwd(ftp_dir)
        f = open(path, "rb")
        ftp.storbinary("STOR " + name, f)
        f.close()
        os.remove(path)
        print("Uploaded")
    finally:
        ftp.quit()
    
keyboard.add_hotkey("shift+0", lambda: handle_keys())
keyboard.wait("alt+end")
