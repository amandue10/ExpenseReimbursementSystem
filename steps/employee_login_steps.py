from behave import Given
from behave import When
from behave import Then


@Given(u'Employee is on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Employee is on the login page')


@When(u'Employee inputs <employee id> into employee Id field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Employee inputs <employee id> into employee Id field')


@When(u'Employee inputs <first name> into first name field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Employee inputs <first name> into first name field')


@When(u'Employee inputs <last name> into last name field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Employee inputs <last name> into last name field')


@When(u'Employee inputs <password> into password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Employee inputs <password> into last name field')


@When(u'Employee clicks submit button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Employee clicks submit button')


@Then(u'Employee should be redirected to the webpage with the title employee page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Employee should be redirected to the webpage with the title employee page')
