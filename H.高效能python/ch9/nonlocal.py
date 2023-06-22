

def outer_function(aa):
    x = 5
    y = 6
    def inner_function():
        nonlocal x
        nonlocal y
        nonlocal aa
        print(x)
        print(y)
        print(aa)
        z = x +y
        print(z)

    inner_function()
    print(x)

outer_function(50)