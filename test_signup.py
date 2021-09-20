import  pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


from pageobjects.Signup import Signuped
from utilities.baseclass import baseclass




class Testtwo(baseclass):
    def test_signup(self,setup,getData):
        log=self.getlogger()
        signup=Signuped(self.driver)
        signup.getname().send_keys(getData["FirstName"])
        log.info("First Name is "+getData["FirstName"])
        signup.getemail().send_keys(getData["email"])
        log.info("Given a valid email address")
        signup.getpassword().send_keys(getData["password"])
        log.info("Setting up a Password")
        signup.clickcheckbox().click()
        self.selectdropdownvalue(signup.getdropdown(),0)
        signup.clickradio().click()
        signup.clicksubmit().click()

        sucesstext = signup.getsuccesstext().text

        assert "Success!" in sucesstext
        self.driver.refresh()

    @pytest.fixture(params=[{"FirstName":"Bhavnish", "email":"bhavnishsharma450@gmail.com","password": "test123*"},
                            {"FirstName":"Avnish", "email":"avnish", "password":"test123*"}])
    def getData(self, request):
        return request.param









