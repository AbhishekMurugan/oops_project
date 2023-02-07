from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class emr():
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

class Add_User(emr):
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


    def element(self):
        try:
            self.driver.find_element(By.ID, "authUUser").click()

        except:
            print("Invalid id")

obj = Add_User()
while True:
    print("Enter 1 for login")
    print("Enter 2 for select only after logging in")
    print("Enter 3 for exception")
    print("Enter 4 for exit code")
    choice = int(input())
    if choice == 1:
        obj.login()
    elif choice == 2:
        obj.user()
    elif choice == 3:
        obj.element()
    elif choice == 4:
        quit()













