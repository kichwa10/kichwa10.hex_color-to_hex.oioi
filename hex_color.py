def to_hex(n):
    digits = "0123456789ABCDEF"
    x = (n % 16)
    ch = ""
    if (x < 10):
        ch = x
    if (x == 10):
        ch = "A"
    if (x == 11):
        ch = "B"
    if (x == 12):
        ch = "C"
    if (x == 13):
        ch = "D"
    if (x == 14):
        ch = "E"
    if (x == 15):
        ch = "F"

    if (n - x != 0):
        return to_hex(n // 16) + str(ch)
    else:
        return str(ch)

def hex_color(red,green,blue):
    x =to_hex(red)
    y =to_hex(green)
    z =to_hex(blue)

    if to_hex(red) in ('a','b','c','d','e','f'):
        x = '0' + x
        return '#'+x+y+z
    elif to_hex(green) in ('a','b','c','d','e','f'):
        y = '0' + y
        return '#'+x+y+z
    elif to_hex(blue) in ('a','b','c','d','e','f'):
        z = '0' + z
        return '#'+x+y+z
    else:
        return '#'+x+y+z

print(hex_color(7,78,155))
