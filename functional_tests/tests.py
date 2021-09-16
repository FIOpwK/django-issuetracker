"""
Functional testing for selenium webdriver on Firefox browser.
Obeying the testing goat
"""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_new_issue_add_retrieve_it_later(self):
        # User Story: Scenario - A user wants to submit a new bug in an issue tracker.
        # Given the users visits the issue tracker homepage
        # When the users opens the homepage
        # Then the homepage should be displayed
        self.browser.get(self.live_server_url)

        # Scenario: A user should be on the issue tracker homepage noted
        # by the title and header elements mentioning Issue-Tracker
        self.assertIn('Issue-Tracker', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Submit new issue', header_text)

        # Scenario: A user is invited to enter a new bug/issue straight away
        inbox = self.browser.find_element_by_id('id_new_issue')
        self.assertEqual(
            inbox.get_attribute('placeholder'),
            'Submit a new issue'
        )

        # Scenario: A user is able to type "Bug in peacock feathers app" into
        # a text box
        # Given the user is typing in the text box
        inbox.send_keys('Bug in peacock feathers app')

        # When the user hits enter
        inbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_issue_table('1 | Bug in peacock feathers app')

        self.fail('Finish the testing!-->')

    # Scenario: A user is greeted with a form element to post
    # Then the page updates and now a new issue has been created
    def wait_for_row_in_issue_table(self, row_text):
        start_time = time.time()
        while True:
            try:

                table = self.browser.find_element_by_id('id_issue_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

        #     # Scenario: A user is able to still add other information
        #     # Given the user has more details to offer
        #     # When the user enters more information of the issue; "Using peacock app crashes"
        #     # Then then page updates again, now showing more details in the ticket(list)
        #

        # Scenario: A user wants to see the site has generate a unique report
        # Given the site has remembered the user's data
        # When the user visits the bug report
        # Then the information entered is still there

        [...]

        # And the user goes back to triage
