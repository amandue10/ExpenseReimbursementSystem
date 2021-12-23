import time

from behave import Given
from behave import When
from behave import Then

from page_object_models.rr_login_page import RRLoginPage


@Given(u'Employee is on the login page')
def step_impl(context):
    context.driver.get(
        "file:///C:/Users/track/OneDrive/Desktop/Revature/ExpenseReimbursementSystem/web_app/HTML/login.html")


@When(u'Employee inputs 1 into employee Id field')
def step_impl(context):
    context.RRLoginPage.select_emp_id_input_box().send_keys(1)


@When(u'Employee inputs Henry into first name field')
def step_impl(context):
    context.RRLoginPage.select_first_name_input_box().send_keys("Henry")


@When(u'Employee inputs Cantu into last name field')
def step_impl(context):
    context.RRLoginPage.select_last_name_input_box().send_keys("Cantu")


@When(u'Employee inputs password into password field')
def step_impl(context):
    context.RRLoginPage.select_password_input_box().send_keys("password")


@When(u'Employee clicks submit button')
def step_impl(context):
    context.RRLoginPage.select_submit_link().click()


@Then(u'Employee should be redirected to the webpage with the title employee page')
def step_impl(context):
    time.sleep(.10)
    assert context.driver.title == "Employee Page"


@Given(u'The logged in employee is on the employee page')
def step_impl(context):
    context.driver.get(
        "file:///C:/Users/track/OneDrive/Desktop/Revature/ExpenseReimbursementSystem/web_app/HTML/employee_page.html")


@When(u'Employee inputs 1 into reimbursement Id field')
def step_impl(context):
    context.RRLoginPage.select_rr_id_input_box().send_keys(0)


@When(u'Employee inputs 1 into logged in employee Id field')
def step_impl(context):
    context.RRLoginPage.select_logged_in_employee_id_input_box().send_keys(1)


@When(u'Employee inputs 1 into manager id field')
def step_impl(context):
    context.RRLoginPage.select_man_id_input_box().send_keys(1)


@When(u'Employee inputs 200 into amount requested field')
def step_impl(context):
    context.RRLoginPage.select_comment_input_box().send_keys(200)


@When(u'Employee inputs comment into comment field')
def step_impl(context):
    context.RRLoginPage.select_comment_input_box().send_keys("Holiday Party")


@When(u'Employee inputs 12/18/2021 into request date field')
def step_impl(context):
    context.RRLoginPage.select_date_input_box().send_keys("12/18/2021")


@When(u'Employee clicks submit button to create a request')
def step_impl(context):
    context.RRLoginPage.select_create_button().click()


@Then(u'the Employee should have created a new reimbursement request')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Employee should have created a new reimbursement request')


@Given(u'The employee is on the employee home page waiting to view all requests')
def step_impl(context):
    context.driver.get(
        "file:///C:/Users/track/OneDrive/Desktop/Revature/ExpenseReimbursementSystem/web_app/HTML/employee_page.html")


@Then(u'The employee should be able to view the reimbursement requests')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The employee should be able to view the reimbursement requests')


@Given(u'The logged in Employee is on the employee page waiting to logout')
def step_impl(context):
    context.driver.get(
        "file:///C:/Users/track/OneDrive/Desktop/Revature/ExpenseReimbursementSystem/web_app/HTML/employee_page.html")


@When(u'The Employee clicks on the logout button')
def step_impl(context):
    context.RRLoginPage.select_employee_logout_link().click()


@Then(u'The Employee should be redirected to the home page')
def step_impl(context):
    time.sleep(.05)
    assert context.driver.title == "Login Page"
