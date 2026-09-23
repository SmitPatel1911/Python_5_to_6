def format_number_short(n):
    if n<1000:
        return str(n)
    elif n<1_000_000:
        return format_number_short(n/1000)+"K"
    else:
        return format_number_short(n/1_000_000)+"M"


print(format_number_short(1500))
print(format_number_short(1200000))
print(format_number_short(500))
