try:
   from colorama import Fore
   import ctypes, pyautogui, keyboard, os, time, platform
   from datetime import datetime
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")


ascii_text = """        ___ _ __   __ _ _ __  
       / __| '_ \ / _` | '_ \ 
       \__ \ | | | (_| | |_) |
       |___/_| |_|\__,_| .__/    
                       |_|    """
                       
def onLinux():
    if platform.system() == "Linux":
        return True
    else:
        return False

class snapchat:

    def __init__(self):
        self.sent_snaps = 0
        self.delay = 0.9

    def get_positions(self):
        self.print_console("Move your mouse to the camera button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.switch_to_camera = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the take picture button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.take_picture = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the arrow down button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.arrow_down = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the Multi Snap button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.multi_snap = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the Edit & Send button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.edit_send = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the Send To button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.send_to = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to your shortcut, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.shortcut = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to select all in shortcut, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.select_all = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to send snap button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.send_snap_button = pyautogui.position()
                break
    
    def send_snap(self, shortcut_users):
        self.update_title(shortcut_users)
        pyautogui.moveTo(self.switch_to_camera)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.take_picture)
        for i in range(7):
            pyautogui.click()
            time.sleep(self.delay)
        pyautogui.moveTo(self.edit_send)
        time.sleep(self.delay)
        pyautogui.click()
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.select_all)
        pyautogui.click()
        pyautogui.moveTo(self.send_snap_button)
        pyautogui.click()
        self.sent_snaps += 7
        self.update_title(shortcut_users)
    
    def update_title(self, shortcut_users):
        now = time.time()
        elapsed = str(now - self.started_time).split(".")[0]
        sent_snaps = self.sent_snaps * shortcut_users
        if onLinux() == False:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Snapchat Score Botter | Sent Snaps: {sent_snaps} | Elapsed: {elapsed}s | Developed by @useragents on Github")

    def print_console(self, arg, status = "Console"):
        print(f"\n       {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
    
    def main(self):
        if onLinux() == False:
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("Snapchat Score Botter | Developed by @useragents on Github")
        else:
            os.system("clear")

        print(Fore.RED + ascii_text)

        self.get_positions()

        # Sometimes ran into "ValueError: invalid literal for int() with base 10: 'fffffffff2'"
        # There should be a better solution for this but I am not a python dev - Chopper1337
        while True:
            try:
                shortcut_users = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] How many people are in this shortcut: "))
                break
            except ValueError:
                print(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] There was an error with that input, please try again :) ")

        self.print_console("Slow PC", "1")
        self.print_console("Fast PC", "2")
        options = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Option: "))
        if options == 1:
            self.delay = 2
        self.print_console("Go to your chats, then press F when you're ready.")
         
        while True:
            if keyboard.is_pressed("f"):
                break
        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED + ascii_text)
        self.print_console("Sending snaps...")
        self.started_time = time.time()
        while True:
            if keyboard.is_pressed("F4"):
                break
            self.send_snap(shortcut_users)
            time.sleep(4)
        self.print_console(f"Finished sending {self.sent_snaps} snaps.")

obj = snapchat()
obj.main()
