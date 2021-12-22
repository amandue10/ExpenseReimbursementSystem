import time

from behave import Given
from behave import When
from behave import Then


@Given(u'Manager is on the login page')
def step_impl(context):
    context.driver.get(
        "file:///C:/Users/track/OneDrive/Desktop/Revature/ExpenseReimbursementSystem/web_app/HTML/login.html")


@When(u'Manager inputs 1 into Manager Id field')
def step_impl(context):
    context.RRLoginPage.select_man_id_input_box().send_keys(1)


@When(u'Manager inputs Amanda into first name field')
def step_impl(context):
    context.RRLoginPage.select_first_name_input_box().send_keys("Amanda")


@When(u'Manager inputs Jones into last name field')
def step_impl(context):
    context.RRLoginPage.select_last_name_input_box().send_keys("Jones")


@When(u'Manager inputs password into password field')
def step_impl(context):
    context.RRLoginPage.select_manager_password_input_box().send_keys("password")


@When(u'Manager clicks submit button')
def step_impl(context):
    context.RRLoginPage.select_manager_submit_link().click()


@Then(u'Manager should be redirected to the webpage with the title Manager page')
def step_impl(context):
    # time.sleep(.20)
    assert context.driver.title == "Manager Page"
