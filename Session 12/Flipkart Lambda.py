from functools import reduce

cart=[499,1299,599,999]

total=reduce(lambda x,y:x+y,cart)

print("Total Price : Rs.",total)
