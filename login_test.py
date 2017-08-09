# Python code to test login page
# Test case: login_testcase.xlsx

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import openpyxl
import unittest
import HTMLTestRunner


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        # Create new Chrome session
        self.driver = webdriver.Chrome("C:\\Users\\dinh_\\PycharmProjects\\Selenium\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        # Navigate to login page
        self.driver.get("http://layerclean.vn/dang-nhap")
        # Should have SIGN IN title
        self.assertIn("SIGN IN", self.driver.title)

    def test_login_submit(self):
        driver = self.driver

        # Open test case files
        wb = openpyxl.load_workbook("C:\\Users\dinh_\\PycharmProjects\\Selenium\\LoginTest\\login_testcase.xlsx")
        sheet = wb.get_active_sheet()
        max_row = sheet.max_row
        # Excel format
        # |---STT---|---Email---|---Password---|---Expected Output---|

        for i in range(1, max_row):
            # Get element
            input_email = driver.find_element_by_id("email")
            input_password = driver.find_element_by_id("pass")
            button_ok = driver.find_element_by_id("login")

            # Get test data in excel

            # Set value to element
            if(sheet)
            input_email.send_keys(sheet["B" + str(i)].value)
            input_password.send_keys(sheet["C" + str(i)].value)
            button_ok.click()

            # Check error
            error = driver.find_element_by_class_name("form-loi")
            self.assertEqual(error.text, sheet["D" + str(i)].value)

    def tearDown(self):
        self.driver.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

if __name__ == "__main__":
    unittest.main()


