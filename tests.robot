*** Settings ***
Library  RFAtomLibray.common.ui.commonUIkeywords
Library  RFAtomLibrary.Apply.EDP1.Apmcommonkeywords

Test Setup  launch_and_logintoapm

*** Variables ***
${url}  https://apm-stg.phenom.com
${browser}  chrome
${username}  shobanbabu.dharavath@phenompeople.com
${password}  11111111111
*** Test Cases ***
testcase1
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate refnum dropdown with data in table
testcase2
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    validate data in table
testcase3
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    validate downloading data in table
tescase4
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Verify Paginations with Show dropdown
testcase5
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate pop up details for Successfull application columns
testcase6
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Verify Search Input with Table Data
testcase7
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Verify Search Input with false Data
testcase8
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Verify Columns in Table
testcase9
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Verify Donwloading Data from table in popup
testcase10
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    verify columns in apply failures tab
testcase11
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    verify pagination with show dropdown in applyfailures
tescase12
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate data in table with Hours Dropdown in apply failures
testcase13
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate Data in Table with Custom Date from calendar in apply failures
testcase14
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Verify Downloading data from table in apply failures
testcase15
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    verify columns in table in APS
testacase16
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Validate Search Input with Data from Table APS
tescase17
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify Data in table with custom Dates APS
testcase18
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify Pagination with Show Dropdown APS
testcase19
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify Labels of Table APS
testcase20
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify Downloading Data from Table APS
testcase21
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Verify Customer name Drop down without submit button APS
testcase22
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate data in table with custom dates AES
testcase23
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate Display Dropdown with area Charts AES
testcase24
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate Display Dropdown with line Charts AES
testcase25
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate Display Dropdown with Pie Charts AES
testcase26
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify All Apply Error Code Pie chart AES
testcase27
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify 2.0 Apply Error Code Pie chart and Failure dropdown with Pie chart
testcase28
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify 1.X Apply Error Code Pie Chart and Failure Dropdown with pie chart
testcase29
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    verify columns in table TBA
testcase30
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    validate data in table with custom dates TBA
testcase31
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    Validate Search Input with Data from Table TBA
testcase32
    [documentation]  navigate to the apply page with valid username and password
    [tags]  functional
    validate_search_input_with_false_data TBA
testcase33
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    verify_pop_up_from_data_in_table TBA
testcase34
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    verify pagination with show dropdown TBA
testcase35
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    verify pagination with show dropdown BAF
testcase36
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Validate Data in Table with refnum and Custom Date Dropdown BAF
testcase37
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify Search Input BAF
testcase38
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    verify search input with false data BAF\
testcase38
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    Verify Downloading Data from Table BFA
testcase39
    [documentation]  navigate to the apply page with valid username and password
    [tags]  UI
    verify columns in table BFA







*** Keywords ***
launch_and_logintoapm
    Launch Browser  url=${url}
    Login to APM  username=${username}  password=${password}