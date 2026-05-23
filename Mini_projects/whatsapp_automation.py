import pyautogui as py
import time

print("welcome to whatsapp automation program")
time.sleep(1)
py.press("win")
time.sleep(1)
py.write("whatsapp")
time.sleep(2)
py.press("enter")
time.sleep(2)
py.hotkey("Ctrl", "f")
time.sleep(1)
py.write("9828293792")
time.sleep(1)
py.press("enter")

assignment="HELLO how are u"
py.write(assignment)
time.sleep(2)
py.press("enter")

print("Thank u for using whatsapp automation")

