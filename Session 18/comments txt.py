comments=["Amazing photo! @rahul_123","Love this @priya","Great content @smit_patel",
          "Follow @fashion_world","Nice post! @amit456","Beautiful! @yaansh_creation",
          "Awesome reel @user_2026","Check this out @tech_guru","Wow! @travel_lover","Amazing work @creative_123"]

with open("instagram_comments.txt", "w") as file:
    file.write("\n".join(comments))

print("File created successfully.")

import re

with open("instagram_comments.txt","r") as file:
    text=file.read()

usernames=re.findall(r"@[A-Za-z0-9_]{3,}",text)

unique_usernames=set(usernames)

print("Unique Instagram usernames : ")

for username in unique_usernames:
    print(username)
