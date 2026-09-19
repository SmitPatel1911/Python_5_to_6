steps=[7500,8200,9500,10500,9800,12000,11000]
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

i=0

while True:
    if steps[i]>10000:
        print("First day you crossed 10,000 steps:",days[i])
        print("Steps:",steps[i])
        break
    i+=1
