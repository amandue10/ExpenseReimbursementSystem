from behave import Given
from behave import When
from behave import Then


@Given(u'The manager is on the Manager page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The manager is on the Manager page')


@When(u'The manager clicks on the logout button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The manager clicks on the logout button')


@Then(u'The manager should be redirected to the home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The manager should be redirected to the home page')
