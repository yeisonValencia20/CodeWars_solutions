# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

## MI CODIGO
def rgb(r, g, b):
    rgb = [r, g, b]
    hexadecimal = ''
    for i in rgb:
        if(i <= 0 ):
            hexadecimal += '00'
            continue
        if(i > 255):
            hexadecimal += 'FF'
            continue
        hexadecimal += '{:02X}'.format(i)
        print(hexadecimal)
    return hexadecimal
    
## CODIGO MEJORES PRACTICAS
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


def rgb(r, g, b):
    clamp = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))