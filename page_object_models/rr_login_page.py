from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class RRLoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # ------------Employee Login functions-------------------

    def select_emp_id_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "idInput")
        return element

    def select_first_name_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "firstNameInput")
        return element

    def select_last_name_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "lastNameInput")
        return element

    def select_password_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "passwordInput")
        return element

    def select_submit_link(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeLoginButton")
        return element

    def get_page_title(self):
        element: WebElement = self.driver.find_element(By.ID, "title")
        return element

    # ------------Manager Login functions-------------------

    def select_man_id_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "managerIdInput")
        return element

    def select_manager_first_name_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "managerFirstNameInput")
        return element

    def select_manager_last_name_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "managerLastNameInput")
        return element

    def select_manager_password_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "managerPasswordInput")
        return element

    def select_manager_submit_link(self):
        element: WebElement = self.driver.find_element(By.ID, "managerLoginButton")
        return element

    def get_manager_page_title(self):
        element: WebElement = self.driver.find_element(By.ID, "title")
        return element




