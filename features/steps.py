from lettuce import *
from nose.tools import assert_equals

"""
Selenium steps to configure behave test scenarios
"""


@step(u'visit url "(.*?)"')
def visit_url(step, url):
    world.browser.get(url)


@step(u'field with name "First Item" ')
def check_first_item(step):
    world.browser.find_element_by_name("li1").click()


@step(u'check if title is "([^"]*)"')
def check_title(step, result):
    title = world.browser.title
    assert_equals(title, result)


@step(u'field with name "Second Item" ')
def check_second_item(step):
    world.browser.find_element_by_name("li3").click()


@step(u'select the textbox add "(.*?)" in the box')
def enter_text(context, text):
    world.browser.find_element_by_id("sampletodotext").click()
    world.browser.find_element_by_id("sampletodotext").clear()
    world.browser.find_element_by_id("sampletodotext").send_keys(text)


@step(u'click the "(.*?)"')
def click_button(context, button):
    world.browser.find_element_by_id(button).click()
