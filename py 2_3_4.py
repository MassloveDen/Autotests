import math
import time
from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id('input_value').text
    y = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element_by_id('answer').send_keys(y)
    # browser.find_element_by_id('robotCheckbox').click()
    # browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()