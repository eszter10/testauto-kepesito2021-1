# 1 Feladat: Pitagorasz-tétel

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)
time.sleep(1)

# elemek megkeresése
a = driver.find_element_by_id("a")
b = driver.find_element_by_id("b")
submit_btn = driver.find_element_by_id("submit")

# tesztadatok listában
test_data_a = ['', '2', '']
test_data_b = ['', '3', '']
test_data_c = ['10', 'NaN']


def test_tc1():
    # * Helyesen jelenik meg az applikáció betöltéskor:
    #     * a: <üres>
    #     * b: <üres>
    #     * c: <nem látszik>
    result = driver.find_element_by_id('result').text
    assert len(result) == 0


def test_tc2():
    # * Számítás helyes, megfelelő bemenettel
    #     * a: 2
    #     * b: 3
    #     * c: 10
    a.send_keys(test_data_a[1])
    b.send_keys(test_data_b[1])
    submit_btn.click()
    time.sleep(0.1)
    result = driver.find_element_by_id("result").text
    assert result == test_data_c[0]


def test_tc_3():
    # * Üres kitöltés:
    #     * a: <üres>
    #     * b: <üres>
    #     * c: NaN
    a.clear()
    b.clear()
    time.sleep(0.1)
    a.send_keys(test_data_a[2])
    b.send_keys(test_data_b[2])
    submit_btn.click()
    time.sleep(0.1)
    result = driver.find_element_by_id("result").text
    assert result == test_data_c[1]

    driver.quit()

