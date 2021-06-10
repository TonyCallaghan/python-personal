import pyautogui
import time

x = True
while x == True: # Move mouse in a square.
	pyautogui.moveTo(400, 400, duration=0.25)
	pyautogui.moveTo(600, 400, duration=0.25)
	pyautogui.moveTo(600, 600, duration=0.25)
	pyautogui.moveTo(400, 600, duration=0.25)
	time.sleep(8) # stop for 8 seconds, gives chance to exit programme
