import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Testemr:
    @pytest.fixture
    def driver(self, request):
        driver = webdriver.Chrome()
        driver.get("https://demo.openemr.io/b/openemr")
        driver.maximize_window()
        driver.implicitly_wait(30)
        request.addfinalizer(driver.quit)
        return driver

    def test_login(self, driver):
        driver.find_element(By.ID, "authUser").send_keys("admin")
        driver.find_element(By.ID, "clearPass").send_keys("pass")
        select_lan = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text("English (Indian)")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.XPATH, "//div[@class='menuLabel px-1 dropdown-toggle oe-dropdown-toggle']").click()
        expected_header = 'Calendar'
        element = driver.find_element(By.XPATH, "//span[text()='Calendar']")
        assert expected_header in element.text
