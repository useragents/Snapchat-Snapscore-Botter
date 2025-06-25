#import sys, platform ,os,pyautogui,keyboard, time
#from colorama import Fore, init


tutorial_video = "https://www.youtube.com/watch?v=hHtRoHRPxag"
version = "1.0.3"
credits = "github.com/useragents"

#CUSTOMIZE SETTINGS:

loop_delay = 5     #This is how many seconds it waits before starting a new loop.
click_delay = 1.2  #This is how many seconds it waits before clicking the mouse between each button. For example it clicks Send To, waits X seconds, then clicks your Shortcut, etc.


position_delay = 0.5 #I would recommend do not touch this. Does not affect the speed of the bot itself.



#DISCLAIMER
#DISCLAIMER
#DISCLAIMER

"""
DISCLAIMER:

I, the developer, am not responsible for any consequences resulting from the use or misuse of this script.
This tool is not affiliated with, endorsed by, or supported by Snapchat Inc. in any way.
Use of this script may violate Snapchat’s Terms of Service (TOS) and Community Guidelines.
Using automation tools like this may possibly result in your account being permanently banned or disabled.
Proceed at your own risk. This script is made for educational purposes.

"""
a_text = rf"""
  ____                    ____        _   
 / ___| _ __   __ _ _ __ | __ )  ___ | |_ 
 \___ \| '_ \ / _` | '_ \|  _ \ / _ \| __|
  ___) | | | | (_| | |_) | |_) | (_) | |_  {credits}
 |____/|_| |_|\__,_| .__/|____/ \___/ \__| v{version}
                   |_|                    """


required_modules = {
    'colorama': 'from colorama import Fore, init, Style',
    'ctypes': 'import ctypes',
    'pyautogui': 'import pyautogui',
    'keyboard': 'import keyboard',
    'os': 'import os',
    'time': 'import time',
    'platform': 'import platform',
    'datetime': 'from datetime import datetime',
    'sys': 'import sys',
    'requests': 'import requests',

}
missing_modules = []

for module, statement in required_modules.items():
    try:
        exec(statement, globals())
    except ImportError:
        missing_modules.append(module)

if missing_modules:
    print("Error. Unable to import one or more required modules")
    print("Please make sure you open the 'Install_Requirements.bat' file before using this program.")
    print(f"Or watch the YouTube tutorial: {tutorial_video}")
    print("\nFor the Python experts, you are missing the following modules:")
    for mod in missing_modules:
        print(f" - {mod}")
    input()
    sys.exit(1)


init(autoreset=True, convert=True)

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def check_if_latest_version():
    s = requests.Session()
    url = "https://raw.githubusercontent.com/useragents/Snapchat-Snapscore-Botter/refs/heads/main/version.txt"
    try:
        r = s.get(url)
    except:
        return
    try:
        latest_version = r.text.replace("\n", "")
        if latest_version != version:
            clear()
            print(f"Please note before use of this script: There is an updated version available.\n- {credits}\nYour Version: {version}\nLatest Version: {latest_version}\nPress ENTER to go to the main menu.")
            input()
    except:
        return

check_if_latest_version()

def title(x):
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(x)
    else:
        # For Linux/macOS terminals supporting ANSI escape codes:
        sys.stdout.write(f"\33]0;{x}\a")
        sys.stdout.flush()

def nice_print(x, status = "-"):
    print(f"{Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {x}")

class snap_bot:

    def __init__(self):
        self.sent_snaps = 0
        self.first_try = True

    def get_positions(self):
        nice_print("Move your mouse to the Camera button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.switch_to_camera = pyautogui.position()
                break
        time.sleep(position_delay)
        nice_print("Move your mouse to the Send to button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.send_to = pyautogui.position()
                break
        time.sleep(position_delay)
        nice_print("Move your mouse to your Shortcut button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.shortcut = pyautogui.position()
                break
        time.sleep(position_delay)
        nice_print("Move your mouse to the Select All in shortcut button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.select_all = pyautogui.position()
                break
        time.sleep(position_delay)

    def send_snap(self, started_time, shortcut_user_count):
        self.update_title(started_time, shortcut_user_count)
        pyautogui.moveTo(self.switch_to_camera)
        if self.first_try:
            pyautogui.click() #Activates the snap feature, only need to do this once.
            self.first_try = False
        time.sleep(click_delay)
        pyautogui.click() #Takes the snap.
        time.sleep(click_delay)
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(click_delay)
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(click_delay)
        pyautogui.moveTo(self.select_all)
        pyautogui.click()
        time.sleep(click_delay)
        pyautogui.moveTo(self.send_to) #Same position.
        pyautogui.click()
        self.sent_snaps += 1
        self.update_title(started_time, shortcut_user_count)
    
    def update_title(self, started_time, shortcut_user_count):

        now = time.time()
        elapsed = str(now - started_time).split(".")[0]
        new_snaps = self.sent_snaps * shortcut_user_count
        title(f"Snapchat Snapscore Bot v{version} | Sent: {new_snaps} | Elapsed: {elapsed}s | {credits}")

        clear()
        print(Fore.RED + a_text)
        nice_print("Snaps Sent", new_snaps)

def main():
    clear()
    title(f"Snapchat Snapscore Bot v{version} | {credits}")
    print(Fore.RED + a_text)
    nice_print("Start", "1")
    nice_print("Help and Instructions", "2")
    nice_print("Disclaimer", "3")
    try:
        option = int(input(f"\n{Fore.RED}> {Fore.WHITE}"))
    except ValueError:
        return main()
    if option == 1:
        try:
            shortcut_user_count = int(input(f"\n{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] How many people are in your shortcut: "))
        except ValueError:
            return main()
        
        
        obj = snap_bot()
        print()
        obj.get_positions()
        print()
        nice_print("Positions are saved. Go back to the beginning, Press F when you are ready.")
        while True:
            if keyboard.is_pressed("f"):
                break
        clear()
        print(Fore.RED + a_text)
        nice_print("Sending snaps...")
        started_time = time.time()
        while True:
            obj.send_snap(started_time, shortcut_user_count)
            time.sleep(loop_delay)
    elif option == 2:
        print()
        nice_print("This program only works with Snapchat Web.", "-")
        nice_print(f"There is a YouTube tutorial video you can watch for help: {tutorial_video}", "-")
        print()
        nice_print("Instructions:", "-")
        nice_print("On your phone, open Snapchat, create a shortcut with as many people as possible to spam snaps to.", "1")
        nice_print("Download Snapchat Web on a Computer", "2")
        nice_print("Login and allow permissions to your Camera/Microphone/etc", "3")
        nice_print("If you don't have a camera, download OBS Studio and get a virtual camera.", "4")
        nice_print("You may need to restart PC if you only downloaded a virtual camera just now.", "5")
        nice_print("Open this program and select the Start option and begin.", "6")
        nice_print("Press ENTER to go back to the main menu.", "-")
        input()
        return main()
    elif option == 3:
        print()
        nice_print("DISCLAIMER:", "!")
        nice_print("I, the developer, am not responsible for any consequences resulting from the use or misuse of this script.", "-")
        nice_print("This tool is not affiliated with, endorsed by, or supported by Snapchat Inc. in any way.", "-")
        nice_print("Use of this script may violate Snapchat’s Terms of Service (TOS) and Community Guidelines.", "-")
        nice_print("Using automation tools like this may possibly result in your account being permanently banned or disabled.", "-")
        nice_print("Proceed at your own risk. This script is made for educational purposes.", "-")
        nice_print("Press ENTER to go back to the main menu.", "-")
        input()
        return main()
    else:
        return main()


        


if __name__ == "__main__":
    main()
