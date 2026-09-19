price=[500,0,750,900,300,450]

total=0

for i in price:
    if i==0:
        continue
    total+=i
    if total>2000:
        break
print("Your Total Is : ",total)
