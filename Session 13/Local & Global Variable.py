x="global"

def outer():
    x="outer"

    def inner():
        nonlocal x
        x="inner"

    inner()
    print("Inside outer:",x)


outer()
print("Outside : ",x)
