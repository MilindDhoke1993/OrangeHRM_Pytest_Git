import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Class
from utilities import ExcelUtils
from utilities.LoggerFile import LogGenerator
from utilities.readConfig import ReadConfig_Class

class Test_OrangeHRM_Login_DDT:

    log = LogGenerator.loggen()
    File_Path=".\\testCases\\Test_Data\\Test_Data.xlsx"

    def test_orangehrm_url_DDT(self,setup):
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
            # assert True
        else:
            print("The link is not working")
        # self.driver.quit()

    def test_orangehrm_login_DDT(self, setup):
        self.driver=setup
        self.lp = Login_Class(self.driver)

        self.rows= ExcelUtils.getrowCount(self.File_Path, "Login_Data")
        print("Number of rows in excel test data:",self.rows)

        List_status=[]

        for i in range(2,self.rows+1):
            self.username = ExcelUtils.readData(self.File_Path,"Login_Data",i,2)
            self.password = ExcelUtils.readData(self.File_Path, "Login_Data", i, 3)
            self.Excel_Result = ExcelUtils.readData(self.File_Path,"Login_Data",i,4)
            print("Username =",self.username)
            print("Password =",self.password)
            print("Expected Result =",self.Excel_Result)
            # time.sleep(2)
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            time.sleep(2)
            self.lp.Enter_Username(self.username)
            # driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
            self.lp.Enter_Password(self.password)
            time.sleep(1)
            self.lp.Click_LogIn()

            if self.lp.Validate_Login_Status()=="LogInPass" and self.Excel_Result=="Login_Pass":
                List_status.append("Pass")
                ExcelUtils.writeData(self.File_Path,"Login_Data",i,5,"Login_Pass")
                time.sleep(1)
                self.log.info("Taking the screenshot for DDT")
                self.driver.save_screenshot(".\\Screenshot\\test_orangehrm_login_DDT_pass.png") #mostly ss are captured for the failed testcases.
                time.sleep(1)
                print("Into the 1st case")
                # self.driver.save_screenshot("I:\\CREDENCE\\Files\\3. Automation Testing\\Tushar Sir\\Pytest_Demo\\Orange_HRM_Pytest\\Screenshot\\login_failed")
                self.lp.Click_Menu()
                self.lp.Click_LogOut()
                # assert True
            #
            elif self.lp.Validate_Login_Status()=="LogInPass" and self.Excel_Result=="Login_Fail":
                List_status.append("Fail")
                ExcelUtils.writeData(self.File_Path, "Login_Data", i, 5, "Login_Fail")
                self.log.info('Taking the screenshot for DDT')
                time.sleep(1)
                self.driver.save_screenshot(".\\Screenshot\\test_orangehrm_login_DDT_fail.png")
                print("Into the 2nd case")
                # assert False
            #
            elif self.lp.Validate_Login_Status() == "LogInFail" and self.Excel_Result == "Login_Pass":
                List_status.append("Fail")
                ExcelUtils.writeData(self.File_Path, "Login_Data", i, 5, "Login_Fail")
                self.log.info("Testcase_DDT is failed ")
                self.log.info('Taking the screenshot for DDT')
                time.sleep(2)
                self.driver.save_screenshot(".\\Screenshot\\test_orangehrm_login_params_DDT.png")
                print("Into the 3rd Case")
                # assert False
            #
            elif self.lp.Validate_Login_Status() == "LogInFail" and self.Excel_Result == "Login_Fail":
                List_status.append("Pass")
                ExcelUtils.writeData(self.File_Path, "Login_Data", i, 5, "Login_Pass")
                self.log.info("Testcase_DDT is failed ")
                self.log.info('Taking the screenshot for DDT')
                time.sleep(2)
                self.driver.save_screenshot(".\\Screenshot\\test_orangehrm_login_DDT_fail.png")
                print("Into the 4th Case")
                # assert True

        print(List_status)
        if "Fail" not in List_status:
            self.log.info("DDT Test Case Passed")
            assert True
        else:
            self.log.info("DDT Test Case Failed")
            assert False

        self.log.info("Closing the browser for DDT")
        self.log.info('Browser closed for DDT')
        self.driver.quit()