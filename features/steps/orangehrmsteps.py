from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'launch chrome browser')
def launBrowser(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    #raise NotImplementedError(u'STEP: Given launch chrome browser')


@when(u'open orange hrm homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    #raise NotImplementedError(u'STEP: When open orange hrm homepage')


@then(u'verify that the logo present on page')
def verifyLogo(context):
    time.sleep(5)
    status = context.driver.find_element(By.XPATH, "//div[@class='orangehrm-login-branding']//img").is_displayed()
    assert status is True
    #raise NotImplementedError(u'STEP: Then verify that the logo present on page')


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
    #raise NotImplementedError(u'STEP: Then close browser')
