from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://creds.appwrk.com/sign-in/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.Signup("Jasreena Kaur","Bains","jasreenakaur09@gmail.com", "1@Jasreenakaur")
        driver.implicitly_wait(3)
        lp.Signin("jasreenakaur09@gmail.com", "1@Jasreenakaur")
