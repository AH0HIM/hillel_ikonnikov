import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    LOGGING_URL = "https://jira.ithillel.com/secure/Dashboard.jspa"
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")
    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Login to Hillel Jira page")
    def login_to_jira(self):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys("webinar5")
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("webinar5")
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    @allure.step
    def enter_name(self, user_name):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys(user_name)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    @allure.step
    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_BUTTON)).click()

    def at_page(self):
        return 'System Dashboard - Jira - Hillel IT School' in self.driver.title

    @allure.step
    def open(self):
        self.driver.get(self.LOGGING_URL)
        return self

    @allure.step
    def wait_for_text_to_appear(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'" + text + "')]")))
