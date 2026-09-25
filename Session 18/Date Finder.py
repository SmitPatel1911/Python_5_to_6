import re

def check_date(text):

    if re.search(r"\d+/\d+/\d+",text):
        return True
    else:
        return False

print(check_date("My Birthday is on 19/11/2004"))
print(check_date("Today is Friday"))
