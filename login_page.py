from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _sign_up_link="Sign up"
    _first_name="firstName"
    _last_name="lastName"
    _email_field = "email"
    _password_field = "password"
    _sign_up_now_button = "MuiButton-label"
    _terms_conditions ="policy"
    _sign_in="Sign in"
    _sign_in_now = "MuiButton-label"


    def clicksignupLink(self):
        self.elementClick(self._sign_up_link, locatorType="link")

    def enterFirstName(self,name):
        self.sendKeys(name, self._first_name)

    def enterLastname(self, lastname):
        self.sendKeys(lastname,self._last_name)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def selectTermsandCondtions(self):
        self.elementClick(self._terms_conditions,locatorType="name")

    def clickSignupnowButton(self):
        self.elementClick(self._sign_up_now_button,locatorType="class")

    def clickSigninbutton(self):
        self.elementClick(self._sign_in, locatorType="link")

    def clickSigninnowbuuton(self):
        self.elementClick(self._sign_up_now_button,locatorType="class")

    def Signup(self, name, lastname, email , password):
        self.clicksignupLink()
        self.enterFirstName(name)
        self.enterLastname(lastname)
        self.enterEmail(email)
        self.enterPassword(password)
        self.selectTermsandCondtions()
        self.clickSignupnowButton()


    def Signin(self,email,password):
        self.clickSigninbutton()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickSigninnowbuuton()