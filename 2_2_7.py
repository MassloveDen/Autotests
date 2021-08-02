import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


browser.find_element_by_name('firstname').send_keys('M')
browser.find_element_by_name('lastname').send_keys('M')
browser.find_element_by_name('email').send_keys('M')



current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_name = "File_example.txt"
file_path = os.path.join(current_dir, file_name)


element = browser.find_element_by_id("file")
element.send_keys(file_path)
button = browser.find_element_by_css_selector("button.btn")
button.click()
