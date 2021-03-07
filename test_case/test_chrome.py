from selenium import webdriver
import time
import os
import re
import pytest
import pytest_html


def checkSpecialCharacter(strValue):
    if (re.search(r"\-", strValue)):
        return float(strValue.replace('-', '').replace('px', ''))/(-1)
    else:
        return float(strValue.replace('px', ''))


class TestCase():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(
            "D:/webdriver/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    # step 2: Check if the subscription prompt is popped up from the bottom of the page
    def test_bottom(self, setup):
        screenshots = []

        self.driver.get(
            "https://www.afr.com/policy/foreign-affairs/capability-edge-and-keeping-south-china-sea-open-crucial--christopher-pyne-20180924-h15rq9")

        # Check if the subscription prompt is popped up from the bottom of the page based on the bottom
        subscription = self.driver.find_elements_by_class_name('Y7Y5d')[0]
        bottom = subscription.value_of_css_property('bottom')
        screenshots.append(self.driver.get_screenshot_as_png())
        assert checkSpecialCharacter(bottom) == 0

        # save all screen shots
        for i in range(len(screenshots)):
            with open('./images/step2.png', "wb") as f:
                f.write(screenshots[i])

    # after step3 scroll down to the end of the page. step 5: verify if the subscription pop up desappears on the same article
    def test_disappear(self, setup):
        screenshots = []

        self.driver.get(
            "https://www.afr.com/policy/foreign-affairs/capability-edge-and-keeping-south-china-sea-open-crucial--christopher-pyne-20180924-h15rq9")

        # step 3: scroll down the complete body height:
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight)")

        # step 4: wait for 10 seconds
        time.sleep(10)

        # step 5: Verify if the subscription pop up disappears on the same article
        subscription = self.driver.find_elements_by_class_name('Y7Y5d')[0]
        bottom2 = subscription.value_of_css_property('bottom')
        screenshots.append(self.driver.get_screenshot_as_png())
        assert checkSpecialCharacter(bottom2) < 0

        # save all screen shots
        for i in range(len(screenshots)):
            with open('./images/step5.png', "wb") as f:
                f.write(screenshots[i])
