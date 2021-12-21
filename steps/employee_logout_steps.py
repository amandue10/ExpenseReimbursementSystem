from behave import Given
from behave import When
from behave import Then


@Given(u'The user is on the employee page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The user is on the employee page')


@When(u'The user clicks on the logout button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user clicks on the logout button')


@Then(u'The user should be redirected to the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The user should be redirected to the home page')
