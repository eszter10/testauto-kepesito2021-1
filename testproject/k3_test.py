# 3 Feladat: Alfanumerikus mező

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)
time.sleep(1)

# elemek megkeresése
title = driver.find_element_by_id('title')
# error_m = driver.find_element_by_xpath('//form//span[@class="error active"]')

# tesztadatok listában
test_data_title = ['abcd1234', 'teszt233@', 'abcd']
test_error_m = ['Only a-z and 0-9 characters allewed', 'Title should be at least 8 characters; you entered 4.']


# a feladat leírásában az első hibaüzenet: Only a-z and 0-9 characters allewed. - ezt módosítottam

def clear_and_fill_input(element, text):
    element.clear()
    element.send_keys(text)


def test_tc1():
    # * Helyes kitöltés esete:
    #     * title: abcd1234
    #     * Nincs validációs hibazüzenet
    clear_and_fill_input(title, test_data_title[0])
    time.sleep(0.1)
    error_m = driver.find_element_by_xpath('//form//span[@class="error"]').text
    assert len(error_m) == 0


def test_tc2():
    # * Illegális karakterek esete:
    #     * title: teszt233@
    #     * Only a-z and 0-9 characters allewed.
    clear_and_fill_input(title, test_data_title[1])
    time.sleep(0.1)
    error_me = driver.find_element_by_xpath('//form//span[@class="error active"]').text
    assert error_me == test_error_m[0]


def test_tc3():
    # * Tul rövid bemenet esete:
    #     * title: abcd
    #     * Title should be at least 8 characters; you entered 4.
    clear_and_fill_input(title, test_data_title[2])
    time.sleep(0.1)
    error_me = driver.find_element_by_xpath('//form//span[@class="error active"]').text
    assert error_me == test_error_m[1]
    driver.quit()



