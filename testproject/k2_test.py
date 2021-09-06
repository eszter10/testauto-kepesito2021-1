# 2 Feladat: Színes reakció

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)
time.sleep(1)


# elemek megkeresése
def test_tc1():
    # * Helyesen jelenik meg az applikáció betöltéskor:
    # * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
    #     <szín neve> [     ] == [     ]
    test_color_name = driver.find_element_by_id("testColorName").text
    assert len(test_color_name) == 0


def test_tc2():
    # * El lehet indítani a játékot a `start` gommbal.
    #     * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
    start_btn = driver.find_element_by_id("start")
    start_btn.click()
    test_color_name = driver.find_element_by_id("testColorName").text
    assert not len(test_color_name) == 0
    stop_btn = driver.find_element_by_id("stop")
    assert stop_btn.is_enabled()
    stop_btn.click()


def test_tc3():
    # * Eltaláltam, vagy nem találtam el.
    #     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
    #     amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
    #       ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.
    start_btn = driver.find_element_by_id("start").click()
    stop_btn = driver.find_element_by_id("stop").click()
    test_color_name = driver.find_element_by_id("testColorName").text
    random_color_name = driver.find_element_by_id("randomColorName").text
    result_m = driver.find_element_by_id("result").text
    if random_color_name == test_color_name:
        assert result_m == "Correct!"
    else:
        assert result_m == "Incorrect!"

    driver.quit()
