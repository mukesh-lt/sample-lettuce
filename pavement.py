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
    description=("Lettuce Integration with Lambdatest"),
    license="MIT",
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
        with open('config/config.json', 'w') as outfile:
            json.dump(desired_cap_dict, outfile)
    jobs = []
    for i in range(2):
        p = multiprocessing.Process(target=run_behave_test, args=(i,))
        jobs.append(p)
        p.start()
