from RFAtomLibrary import CommonUIKeywords
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from RFAtomLibrary.Apply.commonlocatorsapm import CommonLocatorsAPM
from time import sleep

class ApmCommonKeywords(CommonUIKeywords, BuiltIn):
    """ APM Common keywords"""

    @keyword("Login to APM")
    def login_to_apm(self,
                     username: str,
                     password: str):
        """Login to APM by username and password.

                :return: :raise Exception if login does not happened.
                Examples:
                | Login to APM | username    |   password
                """
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                                   "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
        self.wait_until_element_is_visible(locator="xpath=//div[&class='user-name' and text()='shobanbabu dharavath']",
                                           timeout=30,
                                           error=f'login into api is not completed by provide${username}, and ${password}')

    @keyword("Validate refnum dropdown with datai ntable")
    def validate_refnum_dropdown_with_data_in_table(self,
                                                 username: str,
                                                 password: str):
        self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//div[text='offline apply statistics'")
        sleep(2)
        self.javascript_click(locator="xpath=//span[text()='refnum']")
        self.wait_until_element_is_visible(locator="xpath=//tbody[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'refnum dropdown with data not found')

    @keyword("validate data in table")
    def validate_data_in_table(self,
                              username: str,
                              password: str):
        self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
        sleep(2)
        self.javascript_click(locator="xpath=//div[@class='ant-picker-range-separator']")
        sleep(2)
        self.javascript_click(locator="xpath=//button[text()='submit']")
        self.wait_until_element_is_visible(locator="xpath=//tbody[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'validate data in table is not found')

    @keyword("validate downloading data in the table")
    def validate_downloading_data_in_table(self,
                                           username: str,
                                           password: str):

        self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
        sleep(2)
        self.javascript_click(locator="xpath=//span[text()='refnum']")
        sleep(3)
        self.wait_until_element_is_visible(locator="xpath=//span[text()='download as csv']",
                                           timeout=30,
                                           error=f'downloading data in table is not found')

    @keyword("Verify Paginations with Show Dropdown")
    def Verify_Paginations_with_Show_Dropdown(self
                                              ):
        self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
        sleep(2)
        self.javascript_click(locator="xpath=//div[@class='ant-select-selector'")
        sleep(2)
        self.javascript_click(locator="xpath=//span[text()='submit']")

        self.wait_until_element_is_visible(locator="xpath=//tbody[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'pagination in table is not found')

    @keyword("Validate pop up details for Successfull applications columns ")
    def Validate_pop_up_details_for_Successfull_applications_columns(self,
                                                                     ):
        self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
        self.wait_until_element_is_visible(locator="xpath=//div[text()='Total candidate applications submitted successfully']",
                                           timeout=30,
                                           error=f'successful applications pop up is not found')


obj = ApmCommonKeywords()
obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username="something@phenompeople.com", password="something")

obj.validate_refnum_dropdown_with_data_in_table()

obj.validate_data_in_table()

obj.validate_downloading_data_in_table()

obj.Verify_Paginations_with_Show_Dropdown()

obj.Validate_pop_up_details_for_Successfull_applications_columns()








