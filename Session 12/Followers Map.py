def followers_count(number):
    if number>=1000000:
        return f"{number/1000000:.1f}M"
    elif number>=1000:
        return f"{number/1000:.1f}K"
    else:
        return str(number)

followers=[950,1500,25000,1200000]

formatt=list(map(followers_count,followers))

print(formatt)
