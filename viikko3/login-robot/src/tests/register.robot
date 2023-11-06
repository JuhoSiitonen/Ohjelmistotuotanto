*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  Juho  juho1234
    Input Login Command
    Input Credentials  Juho  juho1234
    Output Should Contain  Logged in

Register With Already Taken Username And Valid Password
    Create User  Juho  juho1234
    Input New Command
    Input Credentials  Juho  juho1234
    Output Should Contain  User with username Juho already exists

Register With Too Short Username And Valid Password
    Input New Command  
    Input Credentials  Ju  juho1234
    Output Should Contain  Username should be atleast 3 characters long
    
Register With Enough Long But Invald Username And Valid Password
    Input New Command
    Input Credentials  juho1234  juho1234
    Output Should Contain  Username should be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  Juho  juho123
    Output Should Contain  Password needs to be more than 7 charcters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  Juho  juhojuho
    Output Should Contain  Password needs to contain other than alphabetic characters