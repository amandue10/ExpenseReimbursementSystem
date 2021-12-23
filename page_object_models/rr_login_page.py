from turtle import title

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

    # ----------------Employee Logout---------------------
    def select_employee_logout_link(self):
        element: WebElement = self.driver.find_element(By.ID, "empLogoutButton")
        return element

    def get_login_page_title(self):
        element: WebElement = self.driver.find_element(By.ID, "title")
        return element

    # ------------------Manager Page-----------------------------
    def select_manager_logout_link(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutButton")
        return element

    # def get_login_page_titles(self):
    #     element: WebElement = self.driver.find_element(By.ID, "title")
    #     return element

    # -----------------Employee View All RR ---------------------------
    def get_all_rr_requests(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeTable")
        return element

    # ------------- Create RR ------------------------------
    def select_rr_id_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementIdInput")
        return element

    def select_logged_in_employee_id_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdInput")
        return element

    def select_manager_id_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "managerIdInput")
        return element

    def select_request_amount_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "requestAmountInput")
        return element

    def select_comment_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeCommentInput")
        return element

    def select_date_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "requestDateInput")
        return element

    def select_create_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createRequestButton")
        return element

    # -------------Manager Update Request ----------------------------------------
    def manager_select_rr_id_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementIdInput")
        return element

    def manager_select_logged_in_employee_id_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdInput")
        return element

    def manager_select_manager_id_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "managerIdInput")
        return element

    def manager_select_request_amount_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "requestAmountInput")
        return element

    def manager_select_comment_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeCommentInput")
        return element

    def manager_select_manager_comment_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "managerCommentInput")
        return element

    def manager_make_decision_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "statusBoxInput")
        return element

    def manager_select_date_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "requestDateInput")
        return element

    def manager_select_update_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateRequestButton")
        return element
