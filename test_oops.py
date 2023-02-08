'''import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class emr():            #parent class
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #self.driver.get("https://demo.openemr.io/b/openemr")
        self.driver.get("https://demo.openemr.io/openemr/interface/login/login.php?site=default")
    def login(self):
        self.driver.find_element(By.ID, "authUser").send_keys("admin")
        self.driver.find_element(By.ID, "clearPass").send_keys("pass")
        select_lan = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text("English (Indian)")
        self.driver.find_element(By.ID, "login-button").click()

class Add_User(emr):  #chlid class
    def user(self):
        self.driver.find_element(By.XPATH, "//div[@class='menuLabel px-1 dropdown-toggle oe-dropdown-toggle']").click()
        self.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
        self.driver.switch_to.frame("pat")
        self.driver.find_element(By.ID, "form_fname").send_keys("abhi")
        self.driver.find_element(By.ID, "form_mname").send_keys("shek")
        self.driver.find_element(By.ID, "form_lname").send_keys("m")
        self.driver.find_element(By.ID, "form_suffix").send_keys("kutty")
        self.driver.find_element(By.NAME, "form_DOB").send_keys("04-12-2000")
        select_Gender = Select(self.driver.find_element(By.NAME, 'form_sex'))
        select_Gender.select_by_visible_text('Male')
        self.driver.find_element(By.ID, "create").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("modalframe")
        self.driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()

#expection handling
    def element(self):
        try:
            self.driver.find_element(By.ID, "authUUser").click()

        except:
            print("Invalid id")

# test cases using pytest and assertions

def test_login():
    obj = Add_User()
    obj.login()
    assert obj.driver.current_url == "https://demo.openemr.io/openemr/interface/main/main_screen.php?auth=login&site=default"

if __name__ == "__main__":
    pytest.main()'''



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
