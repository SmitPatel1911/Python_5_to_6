import re

email="Our Email Id is test.123@example.com or test.69@example.com so you can contact us now"

text=re.sub(r"\w+\.+(\d+)+@+\w+\.\w+","[hidden mail]",email)

print(text)
