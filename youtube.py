import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import by
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest

driver = webdriver.Chrome(service=service(ChromeDriverManager().install()))
driver.get("https://www.selenium.com")
serch = driver.find_element(by.TAG_NAME, "a")
len(serch)

def serchh_test():
    expectedresults = 10
    actualresults = len(serch)
    assert actualresults <= expectedresults



