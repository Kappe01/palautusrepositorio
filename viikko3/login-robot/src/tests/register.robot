*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  nipsu  Nipsu123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  m12343123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  mi  moi12345
    Output Should Contain  Username has to be 3 or more letters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  moi123#  moi12345
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  heihei  moi123
    Output Should Contain  Password needs to be more than 7 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  heimoi  moimoimomoimo
    Output Should Contain  Password has to contain something else than just letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command