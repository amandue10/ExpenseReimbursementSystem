from behave import Given
from behave import When
from behave import Then


@Given(u'Manager is on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Manager is on the login page')


@When(u'Manager inputs <1> into Manager Id field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Manager inputs <1> into Manager Id field')


@When(u'Manager inputs <Henry> into first name field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Manager inputs <Henry> into first name field')


@When(u'Manager inputs <Cantu> into last name field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Manager inputs <Cantu> into last name field')


@When(u'Manager inputs <password> into password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Manager inputs <password> into password field')


@When(u'Manager clicks submit button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Manager clicks submit button')


@Then(u'Manager should be redirected to the webpage with the title Manager home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Manager should be redirected to the webpage with the title Manager home page')

