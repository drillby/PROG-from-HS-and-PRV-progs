import pyperclip as copy_paste
from pynput.keyboard import Key, Controller
import time

klavesnice = Controller()

start = input("Sputit program? Y/N")
if start == "Y" or start == "y":
    shrek_skript = open("dokument.txt", "r")
    for x in shrek_skript:
        time.sleep(1)
        print(x)
        copy_paste.copy(x)
        klavesnice.press(Key.ctrl)
        klavesnice.press("v")
        klavesnice.release(Key.ctrl)
        klavesnice.release("v")
        klavesnice.press(Key.enter)
        klavesnice.release(Key.enter)
else:
    exit()
