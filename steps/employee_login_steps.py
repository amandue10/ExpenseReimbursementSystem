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
