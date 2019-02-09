from paver.easy import *
from paver.setuputils import setup
import multiprocessing
import json
import os


setup(
    name="python-lettuce-todo",
    packages=['features'],
    version="1.0.0",
    url="https://www.lambdatest.com/",
    author="Lambdatest",
    description = ("Lettuce Integration with Lambdatest"),
    license = "MIT",
    author_email="support@lambdatest.com"
)


def run_behave_test(task_id=0):
    sh('TASK_ID=%s lettuce features/test.feature' % (task_id))


@task
def run():
    """

    :return:
    """
    desired_cap_dict = {}
    if "LT_BROWSERS" in os.environ:
        desired_cap_dict = os.environ["LT_BROWSERS"]

    if len(desired_cap_dict) >= 2:
        with open('config/config.json', 'w') as outfile:
            json.dump(desired_cap_dict, outfile)
        jobs = []
        for i in range(2):
            p = multiprocessing.Process(target=run_behave_test, args=(i,))
            jobs.append(p)
            p.start()
    else:
        if "LT_USERNAME" in os.environ and "LT_ACCESS_KEY" in os.environ:
            desired_cap_dict["platform"] = os.environ["LT_PLATFORM"]
            desired_cap_dict["browserName"] = os.environ["LT_BROWSER_NAME"]
            desired_cap_dict["version"] = os.environ["LT_BROWSER_VERSION"]
            desired_cap_dict["resolution"] = os.environ["LT_RESOLUTION"]
            desired_cap_dict["name"] = os.environ["LT_BUILD_NAME"]
            with open('config/config.json', 'w') as outfile:
                json.dump(desired_cap_dict, outfile)

        sh('lettuce features/test.feature')
