from RFAtomLibrary import CommonUIKeywords
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from RFAtomLibrary.Apply.commonlocators import CommonLocators
from RFAtomLibrary.APM.commonlocatorsapm import CommonLocatorsAPM
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
                                           timeout=30)
        if not self.get_webelement("xpath=//div[&class='user-name' and text()='shobanbabu dharavath']").is_displayed():
            self.fail(msg=f'Log in to APM is not completed by provided ${username} and ${password}')
        else:
            print("Login Successful\ntest case 1 is passed")

        @keyword("Validate refnum dropdown withdataintable")
        def validate_refnum_dropdown_withdataintable(self,
                                                     username: str,
                                                     password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath=//div[text='offline apply statistics'")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='refnum']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[text()='refnum']").is_displayed():
                self.fail(msg='validate refnum dropdown with data in table is not found')

            else:
                print("refnum dropdown with data found\ntest case 2 is passed")

        @keyword("validate data intable")
        def validate_data_intable(self,
                                  username: str,
                                  password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
            sleep(2)
            self.javascript_click(locator="xpath=//div[@class='ant-picker-range-separator']")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='submit']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[text()='submit']").is_displayed():
                self.fail(msg='validate data in table is not found')

            else:
                print("data in table found\ntest case 3 is passed")
        @keyword("validate downloading data in the table")
        def validate_downloading_data_in_table (self,
                                                username: str,
                                                password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
            sleep(2)
            self.javascript_click(locator="xpath=//span[text()='refnum']")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='download as csv']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[text()='download as csv']").is_displayed():
                self.fail(msg='downloading data in table is not found')

            else:
                print("downloading data in table found\ntest case 4 is passed")

        @keyword("Verify Search Input with Table Data ")
        def verify_search_input_with_table_data(self,
                                                username: str,
                                                password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
            sleep(2)
            self.javascript_click(locator="xpath=//span[text()='search']")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='Submit']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[text()='Submit']").is_displayed():
                self.fail(msg='data in table is not found')

            else:
                print("data in table found\ntest case 5 is passed")

        @keyword("Verify Search Input with false Data ")
        def verify_search_input_with_false_data(self,
                                                username: str,
                                                password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
            sleep(2)
            self.javascript_click(locator="xpath=//span[text()='search']")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='Submit']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[text()='Submit']").is_displayed():
                self.fail(msg='submit in table is not found')

            else:
                print("submit in table found and false data entered\ntest case 5 is passed")

        @keyword("Verify Paginations with Show Dropdown")
        def Verify_Paginations_with_Show_Dropdown(self,
                                                  username: str,
                                                  password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
            sleep(2)
            self.javascript_click(locator="xpath=//div[@class='ant-select-selection-item'")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='Submit']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[text()='Submit']").is_displayed():
                self.fail(msg='show dropdown in table is not found')

            else:
                print("show dropdown in table is found\ntest case 5 is passed")

        @keyword("Verify Columns in Table")
        def verify_columns_intable(self,
                                   username: str,
                                   password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            self.wait_until_element_is_visible(locator="xpath=//DIV[text()='offline apply statistics']",
                                               timeout=30)

            if not self.get_webelement("xpath=//DIV[text()='offline apply statistics']").is_displayed():
                self.fail(msg='columns in table are not found')

            else:
                print("columns in table are found\ntest case 6 is passed")

        @keyword("Validate pop up details for Successfull applications columns ")
        def Validate_pop_up_details_forSuccessfull_applications_columns(self,
                                                                        username: str,
                                                                        password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='successful applications']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[text()='successful applications']").is_displayed():
                self.fail(msg='successful applications in table is not found')

            else:
                print("successful applications in table is found\ntest case 7 is passed")

        @keyword("Verify Downloading Data from table in pop up")
        def Verify_Downloading_Data_from_tablein_popup(self,
                                                       username: str,
                                                       password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath=//div[text()='offline apply statistics']")
            sleep(3)
            self.javascript_click(locator="xpath=//span[text()='failed applications']")
            sleep(2)
            self.javascript_click(locator="xpath=//div[@class='clickable']")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='Download as csv']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[text()='Download as csv']").is_displayed():
                self.fail(msg='download as csv in table is not found')

            else:
                print("download as csv in table is found\ntest case 8 is passed")


        @keyword("verify columns in apply failures table")
        def verify_columns_intable_applyfailures(self,
                                                 username: str,
                                                 password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath//div[text()='Apply Failures']")
            self.wait_until_element_is_visible(locator="xpath=//div[@class='ant-table-wrapper psdt-table']",
                                               timeout=30)

            if not self.get_webelement("xpath=//div[@class='ant-table-wrapper psdt-table']").is_displayed():
                self.fail(msg='columns in table is not found')

            else:
                print("columns in table is found\ntest case is passed")

        @keyword("Verify Pagination with Show Dropdown in apply failures")
        def verify_pagination_withshow_dropdown_applyfailures(self,
                                                              username: str,
                                                              password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath//div[text()='Apply Failures']")
            sleep(2)
            self.javascript_click(locator="xpath//b[text()='show']")
            self.wait_until_element_is_visible(locator="xpath=//td[@class='ant-table-cell']",
                                           timeout=30)

            if not self.get_webelement("xpath=//td[@class='ant-table-cell']").is_displayed():
                self.fail(msg='pagination in table is not found')

            else:
                print("pagination in table is found\ntest case is passed")

        @keyword("Validate data in table with Hours Dropdown")
        def Validate_data_intable_with_Hours_Dropdown_applyfailures(self,
                                                                    username: str,
                                                                    password: str)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath//div[text()='Apply Failures']")
            sleep(2)
            self.javascript_click(locator="xpath//B[text()='time range']")
            self.wait_until_element_is_visible(locator="xpath=//td[@class='ant-table-cell']",
                                               timeout=30)

            if not self.get_webelement("xpath=//td[@class='ant-table-cell']").is_displayed():
                self.fail(msg='data in table is not found')

            else:
                print("data in table is found\ntest case is passed")
        @keyword("Validate Data in Table with Custom Date from calendar")
        def Validate_Data_inTable_with_CustomDate_from_calendar_applyfailures(self,
                                                                              username: str,
                                                                              password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath//div[text()='Apply Failures']")
            sleep(2)
            self.javascript_click(locator="xpath//B[text()='date range']")
            sleep(2)
            self.javascript_click(locator="xpath//snap[text()='submit']")
            self.wait_until_element_is_visible(locator="xpath=//td[@class='ant-table-cell']",
                                               timeout=30)

            if not self.get_webelement("xpath=//td[@class='ant-table-cell']").is_displayed():
                self.fail(msg='data in table is not found')

            else:
                print("data in table is found\ntest case is passed")

        @keyword("Verify Downloading Data from Table")
        def Verify_Downloading_Data_fromTable_applyfailures(self,
                                                            username: str,
                                                            password: str)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath//div[text()='Apply Failures']")
            sleep(2)
            self.javascript_click(locator="xpath//span[text()='submit'")
            self.wait_until_element_is_visible(locator="xpath=//span[text()='download']",
                                               timeout=30)

            if not self.get_webelement("xpath=//span[@class='download']").is_displayed():
                self.fail(msg='downloaded data in table is not found')

            else:
                print("downloaded data in table is found\ntest case is passed")

        """@keyword("Validate Navigating to the Tenant by clicking on refnum")
        def Validate_Navigating_to_the_Tenant_by_clicking_on_refnum_applyfailures(self,
                                                                                  username: str,
                                                                                  password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath//div[text()='Apply Failures']")
            sleep(2)
            self.javascript_click(locator="xpath//span[text()='refnum'")"""

        @keyword("verify pop up in table")
        def Verify_popup_in_Table_applyfailures(self,
                                                username: str
                                                password: str):
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                "').value ='" + str(username) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            self.driver.execute_script(
                "document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                "').value ='" + str(password) + "'")
            sleep(3)
            self.javascript_click(locator=commonlocatorsAPM.CONTINUE_BUTTON)
            sleep(2)
            self.javascript_click(locator=commomlocatorsAPM.APPLY_CLICK)
            sleep(2)
            self.javascript_click(locator="xpath//div[text()='Apply Failures']")
            sleep(2)
            self.javascript_click(locator="xpath//span[text()='fail'")
            self.wait_until_element_is_visible(locator="xpath=//div[text()='Total candidate applications that are failed to submit successfully']",
                                               timeout=30)

            if not self.get_webelement("xpath=//div[text()='Total candidate applications that are failed to submit successfully']").is_displayed():
                self.fail(msg='pop up in table is not found')

            else:
                print("pop up in table is found\ntest case is passed")



obj = ApmCommonKeywords()
obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.validate_refnum_dropdown_withdataintable(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.validate_data_intable(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.validate_downloading_data_in_table(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_search_input_with_table_data(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_search_input_with_table_data(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_search_input_with_false_data(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.Verify_Paginations_with_Show_Dropdown(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_columns_intable(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.Validate_pop_up_details_forSuccessfull_applications_columns(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.Verify_Downloading_Data_from_tablein_popup(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_columns_intable_applyfailures(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_pagination_withshow_dropdown_applyfailures(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.Validate_data_intable_with_Hours_Dropdown_applyfailures(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.Validate_Data_inTable_with_CustomDate_from_calendar_applyfailures(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.Verify_Downloading_Data_fromTable_applyfailures(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")

"""obj.launch_browser(url="https://apm-stg.phenom.com")
obj.Validate_Navigating_to_the_Tenant_by_clicking_on_refnum_applyfailures(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")
"""
obj.launch_browser(url="https://apm-stg.phenom.com")
obj.Verify_popup_in_Table_applyfailures(username="shobanbabu.dharavath@phenompeople.com", password="Shoban@654")









