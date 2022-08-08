from unittest import TestSuite, TextTestRunner
from test_github_grabber import TestToken, TestUser


class HomePage():
    pass


class ContactPage():
    pass


class Page:
    def __init__(self, home, driver):
        self.home = HomePage(home)
        self.contact = ContactPage()
        self.driver = driver

    @property
    def cur_page(self):
        self.driver.get_page()

    def login(self):
        pass  # Login action
        # click(ID)

    def click(self, ID):
        # self.cur_page.click(ID)
        pass

    def check_contact_page(self):
        assert self.cur_page == self.contact


def url_suite():
    suite = TestSuite()
    suite.addTests(
        (TestUser('test_url_valid'),
         TestUser('test_zgithub_user'))
    )
    suite.addTest(TestToken('test_url_invalid'))
    suite.addTest(TestUser('test_url_valid'))
    return suite


if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(url_suite())
