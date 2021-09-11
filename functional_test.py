"""
Functional testing for selenium webdriver on Firefox browser.
Obeying the testing goat
"""
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_new_issue_add_retrieve_it_later(self):

        # User Story: Scenario - A user wants to submit a new bug in an issue tracker.
        # Given the users visits the issue tracker homepage
        # When the users opens the homepage
        # Then the homepage should be displayed
        self.browser.get('http://localhost:8000')

        # Scenario: A user should be on the issue tracker homepage noted
        # by the title and header elements mentioning Issue-Tracker
        self.assertIn('Issue-Tracker', self.browser.title)
        self.fail('Finish the testing!-->')


        # Scenario: A user is invited to enter a new bug/issue straight away

        # Scenario: A user is able to type "Bug in peacock feathers app" into
        # a text box

        # Given the user is typing in the text box
        # When the user hits enter
        # Then the page updates and how a new issue has been created

        # Scenario: A user is able to still add other information
        # Given the user has more details to offer
        # When the user enters more information of the issue; "Using peacock app crashes"
        # Then then page updates again, now showing more details in the ticket(list)

        # Scenario: A user wants to see the site has generate a unique report
        # Given the site has remembered the user's data
        # When the user visits the bug report
        # Then the information entered is still there

        # And the user goes back to triage

if __name__ == '__main__':
    unittest.main()
