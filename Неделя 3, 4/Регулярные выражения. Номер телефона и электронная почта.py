import re

phone_pattern = re.compile(
    r'((\+?7)|8)?'
    r'((\(([0-9]){3}\))|([0-9]){3}|(( |)\(([0-9]){3}\) )|((|-)([0-9]){3})-)'
    r'(([0-9]{7})|(([0-9]){3})-(([0-9]){2})-(([0-9]){2}))$'
)

mail_pattern = re.compile(
    r'([a-zA-Z])+(((\.([a-zA-Z])+))+)?@'
    r'([a-zA-Z]){2,}(((\.([a-zA-Z]){2,}))+){1,}$')

def check_string(string):
    if phone_pattern.match(string) or mail_pattern.match(string):
        return True
    return False

if __name__ == "__main__":
    print(check_string('+7(916)0000000'))
    print(check_string('abc@abc.ab'))
