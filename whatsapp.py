from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyperclip
import sys

CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\Asus\\AppData\\Local\\Google\\Chrome\\User Data\\whatsapp"
CHROME_DRIVER_PATH = r'C:\Users\Asus\PycharmProjects\1.Web Dev\chromedriver_win32\chromedriver.exe'


def bot():
    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)
    browser = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
    browser.get('https://web.whatsapp.com/')

    browser.maximize_window()

    try:
        if sys.argv[1]:
            with open(sys.argv[1], 'r', encoding='utf8') as file:
                groups = [group.strip() for group in file.readlines()]
    except IndexError:
        with open('../whatsapp_bot/groups.txt', 'r', encoding='utf8') as file:
            groups = [group.strip() for group in file.readlines()]

    with open('../whatsapp_bot/msg.txt', 'r', encoding='utf8') as messages:
        msg = messages.read()

    sleep(10)
    for group in groups:
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        search_box = WebDriverWait(browser, 60 * 5).until(
            EC.presence_of_element_located((By.XPATH, search_xpath))
        )

        search_box.clear()
        pyperclip.copy(group)
        search_box.send_keys(Keys.CONTROL + "v")

        sleep(2)
        browser.find_element_by_class_name('YGe90').click()

        sleep(2)
        msg_xpath = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
        pyperclip.copy(msg)
        msg_xpath.send_keys(Keys.CONTROL + 'v')

        browser.find_element_by_class_name('_4sWnG').click()
