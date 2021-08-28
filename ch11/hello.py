print('Hello World.'.upper())
print('Hello World.'.swapcase())
print("""

    Hello
    World.
    {}
    """.format(42 * 7))

print('Hello World.'.capitalize())
print('Hello World.'.title())
print('Hello World.'.casefold())
x = 42
y = 73
print('the number is {xx} {bb}'.format(xx = 42, bb = 73))
print('the number is {1} {0} {1}'.format(x,y))
x = 42 * 747 * 1000
print('the number is {:,}'.format(x).replace(',','.'))
print('Hello World.')