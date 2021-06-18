import re

pass_validator = re.compile(
    '^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
email_validator = re.compile(
    "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")

password_valid = {
    "password": [
        'at least one uppercase letter: A-Z',
        'at least one lowercase letter: a-z',
        'at least one number: 0-9',
        'at least one of any special character: @#$%^&+='
    ]
}
email_valid_message = {
    "email": [
        'not valid email. needs matching with this pattern "email@test.com'
    ]
}
