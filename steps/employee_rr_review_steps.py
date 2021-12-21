from behave import Given
from behave import When
from behave import Then


@Given(u'The user is on the employee home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The user is on the employee home page')


@When(u'The user views the employee page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user views the employee page')


@Then(u'The user should be able to view the reimbursement requests')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The user should be able to view the reimbursement requests')
