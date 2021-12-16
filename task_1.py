import re

RE_EMAIL_VALID = re.compile(r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}")

def email_parse(email):
    if RE_EMAIL_VALID.findall(email):
        print(re.split('@', email))
    else:
        raise ValueError('Incorrect E-mail: ', email)


email_parse(input('Input e-mail: '))