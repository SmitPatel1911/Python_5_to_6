import re

text="Smit: Phone No. +91-9429611689, Parth: Phone No. +91-7041246844, K: Phone No. +66-45789614282"

phone_no=re.findall(r"\+91-\d{10}",text)
print(phone_no)
