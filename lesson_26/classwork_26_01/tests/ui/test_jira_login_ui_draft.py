from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class TestLogin:

    def test_login_to_jira(self):
        #display.start()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                             options=chrome_options)

        driver.get("https://jira.ithillel.com/secure/Dashboard.jspa")
        assert 'System Dashboard - Jira - Hillel IT School' in driver.title

        driver.find_element_by_id("login-form-username").clear()
        driver.find_element_by_id("login-form-username").send_keys("webinar5")
        driver.find_element_by_id("login-form-password").clear()
        driver.find_element_by_id("login-form-password").send_keys("webinar5")
        driver.find_element_by_id("login").submit()

        profile_logo_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "header-details-user-fullname")))
        assert profile_logo_element.is_displayed()
        driver.close()

    def test_mytest(self):
        assert 1 == 1
