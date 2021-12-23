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


@Then(u'Manager should be redirected to the webpage with the title Manager Request Page')
def step_impl(context):
    time.sleep(.05)
    assert context.driver.title == "Manager Request Page"


@Given(u'The manager is on the manager home page')
def step_impl(context):
    context.driver.get("file:///C:/Users/track/OneDrive/Desktop/Revature/ExpenseReimbursementSystem/web_app/HTML"
                       "/manager_page.html")


@When(u'manager inputs 6 into reimbursement Id field')
def step_impl(context):
    context.RRLoginPage.manager_select_rr_id_input_box().send_keys(6)


@When(u'manager inputs 3 into logged in employee Id field')
def step_impl(context):
    context.RRLoginPage.manager_select_logged_in_employee_id_input_box().send_keys(3)

@When(u'manager inputs 1 into logged in manager Id field')
def step_impl(context):
    context.RRLoginPage.manager_select_manager_id_input_box().send_keys(1)


@When(u'manager inputs 200 into amount requested field')
def step_impl(context):
    context.RRLoginPage.manager_select_manager_id_input_box().send_keys(200)


@When(u'manager inputs employee comment into comment field')
def step_impl(context):
    context.RRLoginPage.manager_select_comment_input_box().send_keys("birthday party")

@When(u'manager inputs manager comment into comment field')
def step_impl(context):
    context.RRLoginPage.manager_select_manager_comment_input_box().send_keys("I made this decision...")

@When(u'manager chooses approved status from drop down box')
def step_impl(context):
    context.RRLoginPage.manager_make_decision_input_box().send_keys("approved-completed")

@When(u'manager inputs 12/18/2021 into request date field')
def step_impl(context):
    context.RRLoginPage.manager_select_date_input_box().send_keys("12/18/2021")

@When(u'manager clicks submit button to create a request')
def step_impl(context):
    context.RRLoginPage.manager_select_update_button().click()

@Then(u'the manager should have updated the reimbursement request')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the manager should have updated the reimbursement request')


@Given(u'The logged in manager is on the Manager page')
def step_impl(context):
    context.driver.get("file:///C:/Users/track/OneDrive/Desktop/Revature/ExpenseReimbursementSystem/web_app/HTML"
                       "/manager_page.html")


@When(u'The manager clicks on the logout button')
def step_impl(context):
    context.RRLoginPage.select_manager_logout_link().click()


@Then(u'The manager should be redirected to the home page')
def step_impl(context):
    time.sleep(.05)
    assert context.driver.title == "Login Page"
