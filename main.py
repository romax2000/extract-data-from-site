import profile
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

URL = 'https://ab.onliner.by/bmw/5-seriya?year%5Bfrom%5D=2002&year%5Bto%5D=2003'


# open page with selenium
# (first need to download Chrome webdriver, or a firefox webdriver, etc)
# driver = webdriver.Chrome('/home/user/Документы/Python/Pandas data extract/chromedriver_linux64/chromedriver')
# driver.get(URL)

driver = webdriver.Firefox(executable_path='/home/user/Документы/Python/Pandas data extract/geckodriver-v0.27.0-linux64/geckodriver')
driver.get(URL)
count = driver.find_elements_by_class_name('vehicle-form__offers-unit')
result=0
i=1
for _ in count:
    inf = driver.find_element_by_css_selector(f'#list > div.vehicle-form__offers > div > a:nth-child({i}) > div > div > div.vehicle-form__offers-part.vehicle-form__offers-part_price > div.vehicle-form__description.vehicle-form__description_middle.vehicle-form__description_primary.vehicle-form__description_font-weight_bold.vehicle-form__description_condensed-other').text
    print(inf)
    inf = inf.replace(" ", "")
    inf = inf.replace("р.", "")
    result += int(inf)
    i += 1
# enter sequence into the query field and hit 'blast' button to search
driver.close()
print(f'result = {result / i}')


# open 'Save as...' to save html and assets
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)
# pyautogui.typewrite('site')
# pyautogui.hotkey('enter')
# time.sleep(1)
# pyautogui.hotkey('alt', 'f4')

