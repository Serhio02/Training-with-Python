import pyperclip, re

strong_pwd_regex = re.compile(r'(A-Za-z)(0-9) + {8,}')

password = str(pyperclip())
matches = []

for groups in strong_pwd_regex.findall(password):
    if len(matches) < 8:
        print('Password needs to be at least 8 characters long.')

