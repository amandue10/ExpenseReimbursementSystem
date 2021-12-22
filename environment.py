from behave.runner import Context
from selenium import webdriver
from page_object_models.rr_login_page import RRLoginPage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.RRLoginPage = RRLoginPage(context.driver)


def after_all(context):
    context.driver.quit()

