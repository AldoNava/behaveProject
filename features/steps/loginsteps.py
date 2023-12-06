from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'I launch Firefox browser')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    #raise NotImplementedError(u'STEP: Given I launch Firefox browser')


@when(u'I open orange HRM home page')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    #raise NotImplementedError(u'STEP: When I open orange HRM home page')


@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)


    #raise NotImplementedError(u'STEP: When Enter username "admin" and password "admin123"')

@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then(u'User must successfully login to dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    except Exception as e:
        print(e)
        context.driver.close()
        assert False, "Test failed"

    if text == 'Dashboard':
        context.driver.close()
        assert True, 'Test passed'


    #raise NotImplementedError(u'STEP: Then User must successfully login to dashboard page')