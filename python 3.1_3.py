import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

try:


    x = browser.find_element_by_id('num1').text

    y = browser.find_element_by_id('num2').text




    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(value=str(int(x) + int(y)))

    button = browser.find_element_by_css_selector(".btn")

    button.click()

finally:
    time.sleep(10)
    browser.quit()