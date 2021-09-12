"""
Functional testing for selenium webdriver on Firefox browser.
Obeying the testing goat
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Submit new issue', header_text)


        # Scenario: A user is invited to enter a new bug/issue straight away
        inputbox = self.browser.find_element_by_id('id_new_issue')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Submit a new issue'
        )

        # Scenario: A user is able to type "Bug in peacock feathers app" into
        # a text box
        # Given the user is typing in the text box
        inputbox.send_keys('Bug in peacock feathers app')

        #When the user hits enter
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        table = self.browser.find_element_by_id('id_issue_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Bug in peacock feathers app' for row in rows),
            "New issue item did not appear in table"
        )

        # Scenario: A user is greeted with a form element to post
        form = self.browser.find_element_by_tag_name('form')
        self.assertIs(form, 'form')

        self.fail('Finish the testing!-->')
        # Then the page updates and how a new issue has been created
        [...]
        



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
