# 4 Feladat: Műveletek karakterekkel

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)
time.sleep(1)

# elemek megkeresése
chr = driver.find_element_by_id("chr").text
op = driver.find_element_by_id("op").text
num = driver.find_element_by_id("num").text
submit_btn = driver.find_element_by_id("submit")

# tesztadat
#test_data_app = '!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def test_tc1():
    # * Helyesen betöltődik az applikáció:
    #     * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
    #       * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
    desc = driver.find_element_by_xpath('/html/body/div/div/p[3]').text
    good_char = desc.replace('', ", ").split(", ") # Helyes karakterek listába gyűjtése
    for char in good_char:
        if char == chr:
        assert not len(char) == 0


def test_tc2():
    # * Megjelenik egy érvényes művelet:
    #     * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
    #     * `op` mező vagy + vagy - karaktert tartlamaz
    #     * `num` mező egy egész számot tartalamaz
    assert chr


def test_tc3():
    # * Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
    #     * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
    #     * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
    #     * A `num` mezőben megjelenő mennyiségű karaktert
    #     * az `result` mező helyes karaktert fog mutatni
    submit_btn.click()
    result = driver.find_element_by_id("result").text
    if op == '+':
        result =
    else:
        result =
    driver.quit()


