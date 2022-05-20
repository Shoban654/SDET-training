from RFAtomLibrary import CommonUIKeywords
from RFAtomLibrary.Apply.deco import keyword
from RFAtomLibrary.Apply.BuiltIn import BuiltIn
from RFAtomLibrary.Apply.studiocommonkeywords import FormStudioCommonKeywords
from RFAtomLibrary.Apply.commonlocatorsapm import CommonLocatorsAPM
from time import sleep

class Apmcommonkeywords(commonUIKeywords,BuiltIn):

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
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.wait_until_element_is_visible(locator="xpath=//div[&class='user-name' and text()='shobanbabu dharavath']",
                                           timeout=30,
                                           error=f'login into api is not completed by provide${username}, and ${password}')


    @keyword("Validate refnum dropdown with data in table")
    def validate_refnum_dropdown_with_data_in_table(self,
                                                 username: str,
                                                 password: str):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
        sleep(2)
        self.javascript_click(locator="xpath=//span[text()='refnum']")
        self.wait_until_element_is_visible(locator="xpath=//tbody[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'refnum dropdown with data not found')

    @keyword("validate data in table")
    def validate_data_in_table(self,
                              username: str,
                              password: str):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
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

        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
        sleep(2)
        self.javascript_click(locator="xpath=//span[text()='refnum']")
        sleep(3)
        self.wait_until_element_is_visible(locator="xpath=//span[text()='download as csv']",
                                           timeout=30,
                                           error=f'downloading data in table is not found')

    @keyword("Verify Paginations with Show Dropdown")
    def Verify_Paginations_with_Show_Dropdown(self
                                              ):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
        sleep(2)
        self.javascript_click(locator="xpath=//div[text()='10'")
        sleep(2)
        self.javascript_click(locator="xpath=//span[text()='submit']")

        self.wait_until_element_is_visible(locator="xpath=//tbody[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'pagination in table is not found')

    @keyword("Validate pop up details for Successfull applications columns ")
    def Validate_pop_up_details_for_Successfull_applications_columns(self,
                                                                     ):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
        self.wait_until_element_is_visible(locator="xpath=//div[text()='Total candidate applications submitted successfully']",
                                           timeout=30,
                                           error=f'successful applications pop up is not found')

    @keyword("Verify Search Input with Table Data ")
    def verify_search_input_with_table_data(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
        sleep(2)
        self.javascript_click(locator="xpath=//span[@class='ant-input']")
        sleep(2)
        self.javascript_click(locator="xpath=//BUTTON[@class='ant-btn submit-btn']")
        self.wait_until_element_is_visible(locator="xpath=//tbody[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'validate data in table is not found')

    @keyword("Verify Search Input with false Data ")
    def verify_search_input_with_false_data(self
                                            ):

        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
        sleep(2)
        self.javascript_click(locator="xpath=//span@class='ant-input']")
        sleep(2)
        self.javascript_click(locator="xpath=//BUTTON[@class='ant-btn submit-btn']")
        self.wait_until_element_is_visible(locator="xpath=//tbody[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'false data entered')

    @keyword("Verify Columns in Table")
    def verify_columns_in_table(self):

        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
        self.wait_until_element_is_visible(locator="xpath=//THEAD[@class='ant-table-thead']",
                                           timeout=30,
                                           error=f'columns in table are not found')

    @keyword("Verify Downloading Data from table in pop up")
    def verify_downloading_data_from_table_in_popup(self):

        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath=//DIV[@id = 'rc-tabs-0-tab-offlineApplyStats']")
        sleep(3)
        self.javascript_click(locator="xpath=//span[text()='ant-table-column-title']")
        sleep(2)
        self.javascript_click(locator="xpath=//div[@class='clickable']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath=//span[text()='Download as csv']",
                                            timeout=30,
                                            error=f'download as csv in table is not found')
    @keyword("verify columns in apply failures table")
    def verify_columns_intable_applyfailures(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply failures']")
        self.wait_until_element_is_visible(locator="xpath=//div[@class='ant-table-thead']",
                                           timeout=30,
                                           error=f'total columns not found')

    @keyword("Verify Pagination with Show Dropdown in apply failures")
    def verify_pagination_with_show_dropdown_apply_failures(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply failures']")
        sleep(2)
        self.javascript_click(locator="xpath//span[text()='10']")

        self.wait_until_element_is_visible(locator="xpath=//td[@class='ant-table-cell']",
                                           timeout=30,
                                           error='pagination in not same as selected in dropdown')

    @keyword("Validate data in table with Hours Dropdown in apply failures")
    def validate_data_in_table_with_hours_dropdown_apply_failures(self):

        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply failures']")
        sleep(2)
        self.javascript_click(locator="xpath//span[text()='Last 2 hours']")
        self.wait_until_element_is_visible(locator="xpath=//td[@class='ant-table-cell']",
                                            timeout=30,
                                            error=f'data in table is not found')
    @keyword("Validate Data in Table with Custom Date from calendar")
    def validate_data_in_table_with_custom_date_from_calendar_applyfailures(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//div[text()='Apply Failures']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[@class='ant-picker ant-picker-range datePic']")
        sleep(2)
        self.javascript_click(locator="xpath//TD[@title='2022-05-16']")
        sleep(2)
        self.javascript_click(locator="xpath//TD[@title='2022-05-17']")
        sleep(2)
        self.javascript_click(locator="xpath//BUTTON[text()='submit']")
        self.wait_until_element_is_visible(locator="xpath=//td[@class='ant-table-cell']",
                                           timeout=30,
                                           error=f'data in table is not not found')


    @keyword("Verify Downloading Data from Table in apply failures")
    def verify_downloading_data_from_table_apply_failures(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//div[text()='Apply Failures']")
        sleep(2)
        self.javascript_click(locator="xpath//span[text()='Last 2 hours']")
        sleep(2)
        self.javascript_click(locator="xpath//BUTTON[text()='submit']")
        self.wait_until_element_is_visible(locator="xpath=//BUTTON[text()='Download']",
                                           timeout=30,
                                           error=f'download data in table is not found')
    @keyword("verify columns in table in APS")
    def verify_columns_in_table_aps(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Platform Statistics']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath=//thead[@class='ant-table-thead']",
                                           timeout=30,
                                           error=f'columns in table are not found')
    @keyword("Validate Search Input with Data from Table APS")
    def validate_search_input_with_data_from_table_aps(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Platform Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//INPUT[@class='ant-input']]")
        sleep(2)
        self.javascript_click(locator="xpath//BUTTON[@class='Submit']")
        sleep(2)
        self.wait_until_element_is_visivble(locator="xpath=//TBody[@class='ant-table-tbody']",
                                            timeout=30,
                                            error=f'data in table is not found')

    @keyword("Verify Data in table with custom Dates APS")
    def verify_data_in_table_with_custom_dates_aps(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Platform Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[@class='ant-picker ant-picker-range datePicker']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[@class='ant-picker-input']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[@title='2022-05-12']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[@class='ant-picker-input ant-picker-input-active']")
        sleep(2)
        self.javascript_click(locator="xpath//TD[@title='2022-05-16']")
        sleep(2)
        self.javascript_click(locator="xpath//BUTTON[@class='Submit']")
        self.wait_until_element_is_visivble(locator="xpath=//TBody[@class='ant-table-tbody']",
                                            timeout=30,
                                            error=f'data in table is not found')

    @keyword("Verify Pagination with Show Dropdown APS")
    def verify_pagination_with_show_dropdown_aps(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Platform Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[@class='ant-select-selector']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[@SPAN='10']")
        sleep(2)
        self.wait_until_element_is_visivble(locator="xpath=//TBody[@class='ant-table-tbody']",
                                            timeout=30,
                                            error=f'paginations are not shown upto the selected show dropdown')

    @keyword("Verify Labels of Table APS")
    def verify_labels_of_table_aps(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Platform Statistics']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath=//DIV[@text='Data Center: All    Apply Version: All']",
                                            timeout=30,
                                            error=f'labels of table are not found')

    @keyword("Verify Downloading Data from Table APS")
    def verify_downloading_data_from_table_aps(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Platform Statistics']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath=//BUTTON[@text()='Download as csv']",
                                           timeout=30,
                                           error=f'downloading is not happening')

    @keyword("Verify Customer name Drop down without submit button APS")
    def verify_customer_name_drop_down_without_submit_button_aps(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Platform Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='ALL']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='RBOCCA (RBOCCA)']")
        sleep(2)
        self.javascript_click(locator="xpath//div[text()='Apply Failures']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Platform Statistics']")
        sleep(2)
        self.wait_until_element_is_visible(locaotr="xpath//DIV[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'data is loaded')

    @keyword("Validate data in table with custom dates AES")
    def validate_data_in_table_with_custom_dates_aes(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Error Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//DIV[@class='ant-picker ant-picker-range datePicker']")
        sleep(2)
        self.javaScript_click(locator="xpath//TD[@title='2022-05-12']")
        sleep(2)
        self.javascript_click(locator="xpath//TD[@title='2022-05-18']")
        sleep(2)
        self.javascript_click(locator="xpath//BUTTON[TEXT()='Submit']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//TD[@class='ant-table-cell']",
                                           timeout=30,
                                           error=f'data in table is not in the date range')

    @keyword("Validate Display Dropdown with area Charts AES")
    def validate_display_dropdown_with_area_charts_aes(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Error Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Table']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Area Chart']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//DIV[@id='area-chart']",
                                           timeout=30,
                                           error=f'area chart is not visible')

    @keyword("Validate Display Dropdown with line Charts AES")
    def validate_display_dropdown_with_line_charts_aes(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Error Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Table']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Line Chart']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//DIV[@id='line-chart']",
                                           timeout=30,
                                           error=f'line chart is not visible')
    @keyword("Validate Display Dropdown with Pie Charts AES")
    def validate_display_dropdown_with_pie_charts_aes(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Error Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Table']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Pie Chart']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//DIV[@id='pie-chart']",
                                           timeout=30,
                                           error=f'Pie chart is not visible')
    @keyword("Verify All Apply Error Code Pie chart AES")
    def verify_all_apply_error_code_pie_chart_aes(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Error Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Table']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Pie Chart']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//DIV[text()='All Apply Error CodeTotal ApplicationsALLTotal Errors']",
                                           timeout=30,
                                           error=f'data is not visible in pie chart')

    @keyword("Verify 2.0 Apply Error Code Pie chart and Failure dropdown with Pie chart")
    def verify_2_apply_error_code_pie_chart_and_failure_dropdown_with_pie_chart(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Error Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Table']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Pie Chart']")
        sleep(2)
        self.wait_until_element_is_visible(
            locator="xpath//DIV[text()='2.0 Apply Error CodeTotal ApplicationsALLTotal Errors']",
            timeout=30,
            error=f'data is not found in pie chart')

    @keyword("Verify 1.X Apply Error Code Pie Chart and Failure Dropdown with pie chart ")
    def verify_1_apply_error_code_pie_chart_and_failure_dropdown_with_pie_chart(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Apply Error Statistics']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Table']")
        sleep(2)
        self.javascript_click(locator="xpath//SPAN[text()='Pie Chart']")
        sleep(2)
        self.wait_until_element_is_visible(
            locator="xpath//DIV[text()='1.X Apply Error CodeTotal ApplicationsALLTotal Errors']",
            timeout=30,
            error=f'data is not found in pie chart')
    @keyword("verify columns in table TBA")
    def verify_columns_in_table_tba(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Taleo Bulk Apply']")
        sleep(3)
        self.wait_until_element_is_visible(locator="xpath//DIV[text()='Refnum Completed Runs Processing Runs Failed Runs Data Center']",
                                           timeout=30,
                                           error=f'columns in table are not found')

    @keyword("validate data in table with custom dates TBA")
    def validate_data_in_table_with_custom_date_tba(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Taleo Bulk Apply']")
        sleep(3)
        self.javascript_click(locator="xpath//DIV[text()='ant-picker ant-picker-range datePicker']")
        sleep(2)
        self.javascript_click(locator="xpath//TD[text()='2022-05-12']")
        sleep(2)
        self.javascript_click(locator="xpath//TD[text()=2022-05-18]")
        sleep(2)
        self.javascript_click(locator="xpath//BUTTON[text()='Submit']]")
        self.wait_until_element_is_visible(locator="xpath//TBODY[@class=ant-table-tbody]",
                                           timeout=30,
                                           error=f'data in table is not found')

    @keyword("Validate Search Input with Data from Table TBA")
    def validate_search_input_with_data_from_table_tba(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Taleo Bulk Apply']")
        sleep(3)
        self.javascript_click(locator="xpath//INPUT[@class='ant-input']")
        sleep(3)
        self.javascript_click(locator="xpath//BUTTON[text()='Submit']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//TBODY[@class=ant-table-tbody]",
                                           timeout=30,
                                           error=f'data in table is not found')

    @keyword("Validate search input with false data TBA")
    def validate_search_input_with_false_data_tba(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Taleo Bulk Apply']")
        sleep(3)
        self.javascript_click(locator="xpath//INPUT[@class='ant-input']")
        sleep(3)
        self.javascript_click(locator="xpath//BUTTON[text()='Submit']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//TBODY[@class=ant-table-tbody]",
                                           timeout=30,
                                           error=f'data in table is found')
    @keyword("Verify pop up from data in table TBA")
    def verify_pop_up_from_data_in_table_tba(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Taleo Bulk Apply']")
        sleep(3)
        self.javascript_click(locator="xpath//SPAN[text()='Completed Runs']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//DIV[text()='Click to sort descending']",
                                           timeour=30,
                                           error=f'pop up is not found')

    @keyword("verify pagination with show dropdown TBA")
    def verify_pagination_with_show_dropdown_tba(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Taleo Bulk Apply']")
        sleep(3)
        self.javascript_click(locator="xpath//DIV[@class='ant-select-selector']")
        sleep(3)
        self.javascript_click(locator="xapth//DIV[text()='10']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//TD[@class='ant-table-cell']",
                                           timeout=30,
                                           error=f'pagination is not same as selected')

    @keyword("verify pagination with show dropdown BAF")
    def verify_pagination_with_show_dropdown_baf(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Bulk Apply Failures']")
        sleep(3)
        self.javascript_click(locator="xpath//SPAN[text()='ant-select-selection-item']")
        sleep(3)
        self.javascript_click(locator="xpath//DIV[text()='10']")
        sleep(2)
        self.wait_unitl_element_is_visible(locator="xpath//TBODY[@class='ant-table-tbody']",
                                           timeout=30,
                                           error=f'pagination is not same as selected')

    @keyword("Validate Data in Table with refnum and Custom Date Dropdown BAF")
    def validate_data_in_table_with_refnum_and_custom_date_dropdown_baf(self):

        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Bulk Apply Failures']")
        sleep(3)
        self.javascript_click(locator="xpath//DIV[text()='EQUIGLOBAL']")
        sleep(2)
        self.javascript_click(locator="xpath//INPUT[text()='19 May 2022']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//TBODY[@class='ant-table-tbody']",
                                            timeout='30',
                                            error=f'data not found in table')

    @keyword("Verify Search Input BAF")
    def verify_search_input_bfa(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Bulk Apply Failures']")
        sleep(3)
        self.javascript_click(locator="xpath//INPUT[@class='ant-input']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//INPUT[@class='ant-table-tbody']",
                              timeout='30',
                              error=f'data is not same as data entered in search bar')

    @keyword("verify search input with false data BAF")
    def verify_search_input_with_false_data_baf(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Bulk Apply Failures']")
        sleep(3)
        self.javascript_click(locator="xpath//INPUT[@class='ant-input']")
        sleep(2)
        self.wait_until_element_is_visible(locator="xpath//INPUT[@class='ant-table-tbody']",
                              timeout='30',
                              error=f'data is as data entered in search bar')
    @keyword("Verify Downloading Data from Table BFA")
    def verify_downloading_data_from_table_bfa(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Bulk Apply Failures']")
        sleep(3)
        self.wait_until_element_is_visible(locator="xpath//SPAN[text()=Download]",
                                           timeour='30',
                                           error=f'data is not downloaded')

    @keyword("verify columns in table BFA")
    def verify_columns_in_table_bfa(self):
        self.javascript_click(locator=CommonLocatorsAPM.APPLY_CLICK)
        sleep(2)
        self.javascript_click(locator="xpath//DIV[text()='Bulk Apply Failures']")
        sleep(3)
        self.wait_until_element_is_visible(locator="xpath//THEAD[@class='ant-table-thead']",
                                           timeout='30',
                                           error='columns in table are not found')


obj = ApmCommonKeywords()
obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username="something@phenompeople.com", password="something")


obj.validate_refnum_dropdown_with_data_in_table()

obj.validate_data_in_table()

obj.validate_downloading_data_in_table()

obj.verify_Paginations_with_Show_Dropdown()

obj.validate_pop_up_details_for_successfull_applications_columns()

obj.verify_search_input_with_table_data()

obj.verify_search_input_with_table_false_data()

obj.verify_downloading_data_from_table_in_popup()

obj.verify_columns_in_table()

obj.verify_columns_intable_applyfailures()

obj.verify_pagination_with_show_dropdown_applyfailures()

obj.validate_data_in_table_with_hours_dropdown_apply_failures()

obj.validate_data_in_table_with_custom_date_from_calendar_applyfailures()

obj.verify_downloading_data_from_table_apply_failures()

obj.verify_columns_in_table_aps()

obj.validate_search_input_with_data_from_table_aps()

obj.verify_data_in_table_with_custom_dates_aps()

obj.verify_pagination_with_show_dropdown_aps()

obj.verify_labels_of_table_aps()

obj.verify_downloading_data_from_table_aps()

obj.verify_customer_name_drop_down_without_submit_button_aps()

obj.validate_data_in_table_with_custom_dates_aes()

obj.validate_display_dropdown_with_area_charts_aes()

obj.validate_display_dropdown_with_line_charts_aes()

obj.validate_display_dropdown_with_pie_charts_aes()

obj.verify_2_apply_error_code_pie_chart_and_failure_dropdown_with_pie_chart()

obj.verify_1_apply_error_code_pie_chart_and_failure_dropdown_with_pie_chart()

obj.verify_columns_in_table_tba()

obj.validate_data_in_table_with_custom_date_tba()

obj.validate_search_input_with_data_from_table_tba()

obj.validate_search_input_with_false_data_tba()

obj.verify_pop_up_from_data_in_table_tba()

obj.verify_pagination_with_show_dropdown_baf()

obj.validate_data_in_table_with_refnum_and_custom_date_dropdown_baf()

obj.verify_search_input_bfa()

obj.verify_search_input_with_false_data_baf()

obj.verify_downloading_data_from_table_bfa()

obj.verify_columns_in_table_bfa()





















