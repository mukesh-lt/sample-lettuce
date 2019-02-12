from paver.easy import *
from paver.setuputils import setup
import multiprocessing
import os
import json

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


def run_lettuce_test(env, index=0):
    """
    runs the individual test
    :param env:
    :param index:
    :return:
    """
    if env == "jenkins":
        sh('INDEX=%s env=%s lettuce features/test.feature ' % (index, env,))
    else:
        sh('INDEX=%s env=%s lettuce features/test.feature ' % (index, env,))


@task
@consume_args
def run(args):
    """
    runs the lettuce test
    :return:
    """
    env = args[0] if len(args) > 0 else ""
    jobs = []
    pool = get_pool_size()
    for i in range(pool):
        p = multiprocessing.Process(target=run_lettuce_test, args=(env, i,))
        jobs.append(p)
        p.start()


def get_pool_size():
    """
    sets the number of parallel test
    :return:
    """
    if "LT_BROWSERS" in os.environ:
        CONFIG = json.loads(os.environ["LT_BROWSERS"])
        pool = len(CONFIG)
    else:
        json_file = "config/config.json"
        with open(json_file) as data_file:
            CONFIG = json.load(data_file)
        pool = len(CONFIG)
    return pool
