import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Tnstc:
    @pytest.fixture
    def driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        request.addfinalizer(driver.quit)
        return driver
    def test_login(self, driver):
        driver.get("https://www.tnstc.in/")
        driver.find_element(By.LINK_TEXT, "E-Ticket Login").click()
        driver.find_element(By.NAME, "txtUserLoginID").send_keys("sudharshan.k234@gmail.com")
        driver.find_element(By.NAME, "txtPassword").send_keys("dharshan")
        driver.find_element(By.XPATH, "//a[@class='dboxheader']").click()