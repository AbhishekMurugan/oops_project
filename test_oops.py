import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class emr:
    @pytest.fixture
    def driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        request.addfinalizer(driver.quit)
        return driver

    def test_login(self, driver):
        driver.get("https://demo.openemr.io/openemr/interface/login/login.php?site=default")
        driver.find_element(By.ID, "authUser").send_keys("admin")
        driver.find_element(By.ID, "clearPass").send_keys("pass")
        select_lan = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text("English (Indian)")
        driver.find_element(By.ID, "login-button").click()
        expected_header = 'ADD PATIENT'
        element = driver.find_element(By.XPATH, "//h[contains(@name,'text--add patient')]")
        assert expected_header in element.text