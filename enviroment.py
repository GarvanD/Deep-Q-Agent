import webbrowser
import pyautogui
from time import sleep
from PIL import Image
from PIL import *
from resizeimage import resizeimage
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\e95645\AppData\Local\Tesseract-OCR\tesseract.exe'
def load_game():
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://garvand.github.io/DiscreteMathStrikesBack/index.html")
    new_game_pos = None
    while new_game_pos is None:
        try:
            new_game_pos = pyautogui.locateOnScreen('title_screen\\new_game.png')
        except ImageNotFoundException:
            pass
    new_game_pos = pyautogui.center(new_game_pos)
    pyautogui.press('enter') 

def screen_shot():
    img = ImageGrab.grab(bbox=(475,250, 975, 550))
    img.save("screenshots\\snapshot.png")
    return img

def process_frame(frame):
    img =  frame.convert('LA')
    img = resizeimage.resize_cover(img, [195, 110])
    img.save("screenshots\\snapshot_reduced.png")
    return img

def get_hero_position():
    hero_position = None
    search_iterations = 0
    while hero_position is None:
        search_iterations += 1
        try:
            hero_position = pyautogui.locateOnScreen('characters\\hero.png')
        except ImageNotFoundException:
            if search_iterations < 25:
                pass
            else:
                return None
        hero_position = pyautogui.center(hero_position)
    return hero_position

def get_score():
    img = ImageGrab.grab(bbox=(1320,275, 100, 40))
    text = pytesseract.image_to_string(img)
    print("Test:" + text)
    return text