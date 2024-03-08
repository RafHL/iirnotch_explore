import numpy as np

def approx(value, digits):
    return fixp2dec(fixp(value, digits))

def fixp(value, digits=np.inf):
    if hasattr(value, "__len__"):
        return [binary(v, -digits) for v in value]
    return binary(value, -digits)

def binary(value, stop=0):
    if value < 0:
        fixp = '-'
        value = abs(value)
    else:
        fixp = ''

    if value >= 1:
        fixp += f"{int(value):b}."
        value -= int(value)
    else:
        fixp += "0."

    if stop >= 0:
        return fixp

    cur_val = 2.**-1
    end_val = 2.**stop

    while cur_val >= end_val and value > 0:
        if (value - cur_val >= 0):
            value -= cur_val
            fixp += "1"
        else:
            fixp += "0"

        cur_val /= 2.

    return fixp

def fixp2dec(value, digits=np.inf):
    if hasattr(value, "__len__"):
        return [unbinary(v, digits) for v in value]
    unbinary(value, digits)

def unbinary(value, digits=0):
    whole, frac = value.split('.')
    decimal = float(abs(int(whole, 2)))

    cur_val = 2.**-1

    for ind,b in enumerate(frac):
        if ind >= digits:
            break

        if b[0] == '1':
            decimal += cur_val

        cur_val /= 2.

    if whole[0] == '-':
        decimal *= -1

    return decimal
