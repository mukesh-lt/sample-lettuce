from lettuce import before, after, world
from selenium import webdriver
import lettuce_webdriver.webdriver
import os
import json

TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
if os.environ["env"] == "jenkins":
    json_env = "config/jenkins.json"
    if os.environ["env"] == "jenkins":
        desired_cap_dict = os.environ["LT_BROWSERS"]
        with open('config/jenkins.json', 'w') as outfile:
            json.dump(desired_cap_dict, outfile)
else:
    json_env = "config/local.json"
with open(json_env) as data_env:
    CONFIG = json.load(data_env)
if os.environ["env"] == "jenkins":
    CONFIG = json.loads(CONFIG)
with open("config/user.json") as data_env:
    USER_CONFIG = json.load(data_env)

username = os.environ["LT_USERNAME"] if "LT_USERNAME" in os.environ else USER_CONFIG["username"]
authkey = os.environ["LT_ACCESS_KEY"] if "LT_ACCESS_KEY" in os.environ else USER_CONFIG["access_key"]


@before.each_feature
def setup(feature):
    desired_cap = setup_desired_cap(CONFIG[TASK_ID])
    world.browser = webdriver.Remote(
        desired_capabilities=desired_cap,
        command_executor="https://%s:%s@hub.lambdatest.com:443/wd/hub" % (username, authkey)
    )


@after.each_feature
def exit(feature):
    world.browser.quit()


def setup_desired_cap(desired_cap):
    if os.environ['env'] == 'jenkins':
        desired_cap["platform"] = desired_cap["operatingSystem"]
        del desired_cap["operatingSystem"]
        desired_cap["version"] = desired_cap["browserVersion"]
        del desired_cap["browserVersion"]
        return desired_cap
