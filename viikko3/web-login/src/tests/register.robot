*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Page Should Contain  Username should be atleast 3 characters long

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password confirmation  kallekalle
    Submit Credentials
    Page Should Contain  Password needs to contain other than alphabetic characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password confirmation  kalle456
    Submit Credentials
    Page Should Contain  Password and confirmation not the same

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle12
    Set Password confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Page Should Be Open

