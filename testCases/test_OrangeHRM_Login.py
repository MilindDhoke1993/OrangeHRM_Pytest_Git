import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Class
from utilities.LoggerFile import LogGenerator
from utilities.readConfig import ReadConfig_Class

class Test_OrangeHRM_Login:
    Username=ReadConfig_Class.getUsername()
    Password=ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    def test_orangehrm_url(self,setup):
        # self.log.debug("This is debug")
        # self.log.info("This is info") #testers mostly use this
        # self.log.warning("This is warning")
        # self.log.error("This is error")
        self.log.critical("Test case is started")

        self.driver=setup
        self.log.info("Opening browser")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        if self.driver.title=="OrangeHRM":
            print('The link is working')
            assert True
        else:
            assert False
        self.driver.quit()

    def test_orangehrm_login(self, setup):
        self.driver=setup
        self.lp = Login_Class(self.driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        print('User Name:',self.Username)
        self.lp.Enter_Username(self.Username)
        # driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        print('Password:',self.Password)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_LogIn()
        if self.lp.Validate_Login_Status()=="LogInPass":
            time.sleep(2)
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshot\\test_orangehrm_login_pass.png") #mostly ss are captured for the failed testcases.

            self.log.info("Testcase is passed")

            # self.driver.save_screenshot("I:\\CREDENCE\\Files\\3. Automation Testing\\Tushar Sir\\Pytest_Demo\\Orange_HRM_Pytest\\Screenshot\\login_failed")
            self.lp.Click_Menu()
            self.lp.Click_LogOut()
            assert True
        else:

            self.log.info("Testcase is failed ")

            time.sleep(2)
            self.log.info('Taking the screenshot')
            self.driver.save_screenshot(".\\Screenshot\\test_orangehrm_login_fail.png")
            assert False

        self.log.info("Closing the browser")
        self.driver.quit()
        self.log.info('Browser closed')
