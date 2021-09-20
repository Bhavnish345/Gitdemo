
import pytest
import time



from pageobjects.home import Homepage
from pageobjects.order import Ordered
from utilities.baseclass import baseclass


class TestOne(baseclass):

    def test_e2e(self,setup):
        home=Homepage(self.driver)
        ordered=Ordered(self.driver)
        home.search().send_keys("to")
        list1 = []
        list2 = []

        time.sleep(4)

        count = len(home.cardselect())

        assert count == 2

        buttons = home.clickcardbuttons()

        for button in buttons:
            list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
            button.click()

        print(list1)
        home.addcart().click()
        home.checkout().click()

        Results = ordered.products()

        for Result in Results:
            list2.append(Result.text)

        print(list2)

        # assert list1 == list2

        totalamount = ordered.total().text
        self.applycapuman("rahulshettyacademy")
        #ordered.enterpromocode().send_keys("rahulshettyacademy")
        ordered.applycaupan().click()

        print(ordered.getpromotext().text)
        discountedamount = ordered.getdiscountamount().text

        print(discountedamount)
        print(totalamount)
        assert float(discountedamount) < int(totalamount)

        amounts = ordered.sum()

        sum = 0

        for amount in amounts:
            sum = sum + int(amount.text)  # 32+48+60

        print(sum)

        printedamount = ordered.totalprinted().text

        assert sum == int(printedamount)


