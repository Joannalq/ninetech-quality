# Exploratory Testing Exercise

In the exploratory testing exercise folder, the scenarios.md lists test scenarios. The discrepancies.md lists the discrepancies found based on validations in the scenarios.md.

# Automation Exercise

## Setting up the environment

### Coding Editor

Visual Studio Code

### Installing Python:

Step 1: Download and install Python (version 3 or above): https://www.python.org/downloads/. For how to install Python, please refer to https://realpython.com/installing-python/.

Step 2: Plug-in installation: For Windows system, run the Command Prompt. Then enter the following command to install the plug-ins.

```
 pip install regex
```

```
 pip install selenium
```

```
 pip install pytest
```

```
 pip install pytest-html
```

### Setting up WebDriver for Chrome

Step 1: Please download the version of Selenium webDriver (ChromeDriver) which is compatible to the Google Chrome browser installed on your computer.

- To check your Google Chrome browser version, on the top right corner of the browser, click the three dot --> Help --> About Google Chrome.
- ChromeDriver download address: https://chromedriver.chromium.org/downloads

Step 2: After downloading ChromeDriver, unzip it to folder, e.g. D:\webdriver.

### Setting up Tests

Step 1: Download the test from GitHub to a folder in your computer, e.g. c:\explorary_test.

Step 2: In the test_chrome.py file under the test_case sub-folder, please change the WebDriver (chromedriver.exe) path under the setup function (around line 19) to the path where WebDriver is unzipped.
eg. self.driver = webdriver.Chrome(
"D:/webdriver/chromedriver_win32/chromedriver.exe")

## Executing Tests

### Test execution and report generation

Step 1: start with Visual Studio Code File -> Open folder to load the whole project

Step 2: Terminal -> New Terminal to open the TERMINIAL window.

Step 3: In the terminal window type the following commands:

```
cd test_case
```

```
pytest -v -s --html=./reports/report.html --self-contained-html test_chrome.py
```

note: --html=./reports/report.html: report.html could be changed to any other file name

### Output Files

After completing the test, the screenshot for step 2 and step 5 will be saved in the images sub-folder（of the test_case folder).

the report (html file) will be saved in the reports sub-folder (of the test_case folder).
