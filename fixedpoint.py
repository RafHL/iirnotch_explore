import numpy as np

def approx(value, digits):
    if not hasattr(value, "__len__"):
        value = [value]
    return fixp2dec(*fixp(*value, digits=digits))

def fixp(*value, digits=np.inf):
    return [binary(v, -digits) for v in value]

def binary(value, stop=0):
    if value < 0:
        fixp = '-'
        value = abs(value)
    else:
        fixp = ''

    fixp += f"{int(value):b}."
    value -= int(value)

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

def fixp2dec(*value, digits=np.inf):
    return [unbinary(v, digits) for v in value]

def unbinary(value, digits=0):
    whole, frac = value.split('.')
    decimal = float(abs(int(whole, 2)))

    if len(frac):
        res = 2**(-len(frac))
        decimal += int(frac,2)*res

    return decimal
