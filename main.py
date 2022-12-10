import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

def find_and_click(picture_path):
    # find the coordinate through the picture_path
    coords = pyautogui.locateOnScreen(picture_path,0.80)
    # move to that coordinate
    pyautogui.moveTo(coords,duration=1)
    # left click
    pyautogui.leftClick()

# login phase
def login():
    # open browser
    pyautogui.hotkey("winleft","1")
    # open a new browser tag
    pyautogui.hotkey("Ctrl","t")

    # Enter the typingclub web side 
    pyautogui.typewrite("www.typingclub.com")
    pyautogui.typewrite(['enter','enter'])

    find_and_click('./image/login_button1.png')
    pyautogui.sleep(2)
    pyautogui.typewrite(['tab','tab','enter'])
    print("login complete!")

# Select class phase
def select_class():
    pyautogui.sleep(2)
    c1 = pyautogui.locateOnScreen(image='./image/select_class0.png',confidence=0.90)
    pyautogui.moveTo(c1)

    c2 = list(pyautogui.locateAllOnScreen(image='./image/start_button.png',confidence=0.90))
    pyautogui.moveTo(c2[3])
    pyautogui.leftClick()


def typing():
    pyautogui.sleep(5)
    with open('./text/538.txt', 'r') as f:
        text = f.readline()
        pyautogui.write(text,interval=0.05)

login()
select_class()
# typing()
