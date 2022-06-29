# Python-Lettuce-Sample

![MSTest](https://opengraph.githubassets.com/897e9d2bff40eb38d71408ba159621baa306b905469b9f11d21ee73fcf6ef795/LambdaTest/sample-lettuce)

## Prerequisites

1. Install pip and python.

```
sudo apt install python-pip
sudo apt install python 2.7.18
```

2. The recommended way to run your tests would be in virtualenv. It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.

```
pip install virtualenv
```

## Steps to Run your First Test

Step 1. Clone the Lettuce-Sample Repository.

```
git clone https://github.com/LambdaTest/sample-lettuce
```

Step 2. Inside Lettuce-Sample folder, export the Lambda-test Credentials. You can get these from your automation dashboard.

<p align="center">
   <b>For Linux/macOS:</b>
   
```
export LT_USERNAME="YOUR_USERNAME"
export LT_ACCESS_KEY="YOUR ACCESS KEY"
```

<p align="center">
   <b>For Windows:</b>
   
```
set LT_USERNAME="YOUR_USERNAME"
set LT_ACCESS_KEY="YOUR ACCESS KEY"
```

Step 3. Next we create and Activate the virtual environment in the Lettuce-Sample folder.

For Linux/MacOS
```
virtualenv venv
source venv/bin/activate
```

For Windows
```
python -m virtualenv venv
venv\Scripts\activate.bat
```

Step 4. Then install required packages.

```
pip install -r requirements.txt
```

### Run tests
##### Running tests
```bash
paver run 
```

##### Running tests through LambdaTest Jenkins Plugin
```bash
paver run jenkins
```

####  Routing traffic through your local machine
- Set tunnel value to `true` in test capabilities
> OS specific instructions to download and setup tunnel binary can be found at the following links.
>    - [Windows](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Windows)
>    - [Mac](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+MacOS)
>    - [Linux](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Linux)

## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.
