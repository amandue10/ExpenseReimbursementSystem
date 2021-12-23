# from behave import Given
# from behave import When
# from behave import Then
#
#
# @Given(u'The employee is on the employee page')
# def step_impl(context):
#     context.driver.get(
#         "file:///C:/Users/track/OneDrive/Desktop/Revature/ExpenseReimbursementSystem/web_app/HTML/employee_page.html")
#
#
# @When(u'Employee inputs 1 into reimbursement Id field')
# def step_impl(context):
#     context.RRLoginPage.select_rr_id_input_box().send_keys(0)
#
#
# @When(u'Employee inputs 1 into manager id field')
# def step_impl(context):
#     context.RRLoginPage.select_emp_id_input_box(1)
#
#
# @When(u'Employee inputs 200 into amount requested field')
# def step_impl(context):
#     context.RRLoginPage.select_man_id_input_box(1)
#
#
# @When(u'Employee inputs comment into comment field')
# def step_impl(context):
#     context.RRLoginPage.select_comment_input_box("Holiday Party")
#
#
# @When(u'Employee inputs 12/18/2021 into request date field')
# def step_impl(context):
#     context.RRLoginPage.select_date_input_box("12/18/2021")
#
#
# @Then(u'the Employee should have created a new reimbursement request')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the Employee should have created a new reimbursement request')
