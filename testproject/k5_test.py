# 5 Feladat: Bingo

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)
time.sleep(1)

# elemek megkeresése
init_btn = driver.find_element_by_id('init')
play_btn = driver.find_element_by_id('spin')


def tc1():
    # * Az applikáció helyesen megjelenik:
    #     * A bingo tábla 25 darab cellát tartalmaz
    #     * A számlista 75 számot tartalmaz
    bingo_cells = driver.find_elements_by_xpath('//tbody[@id="bingo-body"]/tr/td/div')

def tc2():
    # * Bingo számok ellenőzrzése:
    #     * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik

    #     * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki

def tc3():
    # * Új játékot tudunk indítani
    #     * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
    #     * új bingo szelvényt kapunk más számokkal.
    driver.quit()

