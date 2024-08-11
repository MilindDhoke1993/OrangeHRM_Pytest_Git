import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Class:

    Text_UserName_XPATH = (By.XPATH,"//input[@placeholder='Username']")
    Text_Password_XPATH = (By.XPATH,"//input[@placeholder='Password']")
    LogIn_Button_XPATH = (By.XPATH,"//button[@type='submit']")
    Menu_Button_XPATH = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    LogOut_Button_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10) #find the poll frequency

    def Enter_Username(self,username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_UserName_XPATH))
        self.driver.find_element(*Login_Class.Text_UserName_XPATH).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*Login_Class.Text_Password_XPATH).send_keys(password)

    def Click_LogIn(self):
        self.driver.find_element(*Login_Class.LogIn_Button_XPATH).click()

    def Click_Menu(self):
        self.driver.find_element(*Login_Class.Menu_Button_XPATH).click()

    def Click_LogOut(self):
        self.driver.find_element(*Login_Class.LogOut_Button_XPATH).click()

    def Validate_Login_Status(self):
        try:
            time.sleep(2)
            # self.driver.find_element(By.XPATH, *Login_Class.Menu_Button_XPATH)
            self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
            print("Orange HRM Log In Test Case Passed")
            return "LogInPass"

        except:
            print("Orange HRM Log In Test Case Failed")
            return "LogInFail"


