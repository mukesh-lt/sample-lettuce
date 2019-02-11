from lettuce import before, after, world
from selenium import webdriver
import lettuce_webdriver.webdriver
import os
import json

TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
with open("config/config.json") as data_file:
    CONFIG = json.load(data_file)
with open("config/user.json") as data_file:
    USER_CONFIG = json.load(data_file)

username = os.environ["LT_USERNAME"] if "LT_USERNAME" in os.environ else USER_CONFIG["username"]
authkey = os.environ["LT_ACCESS_KEY"] if "LT_ACCESS_KEY" in os.environ else USER_CONFIG["access_key"]
desired_cap = {}


@before.each_feature
def setup(feature):
    desired_cap = CONFIG[TASK_ID]
    world.browser = webdriver.Remote(
            desired_capabilities=desired_cap,
            command_executor="https://%s:%s@hub.lambdatest.com:443/wd/hub" % (username, authkey)
    )




@after.each_feature
def exit(feature):
    world.browser.quit()
