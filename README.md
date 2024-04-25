# Notch Exploration Exercise
RafHL

## Summary
This is my implementation of a [fixedpoint library](/fixedpoint.py) in Python
which I used to explore what would happen if I try to approximate an
[iirnotch](/notch.py) as seen in [notch_approx](/notch_approx.py).

My first attempt is [all_notch_approx](/all_notch_approx.py), where I posted all
the estimations on a single plot. In [split notch approx](/split_notch_approx.py),
I post 6 graphs with 10 different bit estimations inside. In
[notch_approx](/notch_approx.py), I used a slider to change the number of bits.
Be warned that this script makes a ~7 GB pickle file with all the different
magnitude response approximations.

## Directions
Fixedpoint:
- approx(value, digits) rounds `value` to `digits` bit fractional places, value can be a list or a single value
- fixp(value[, value, ..., digits=<fractional bits wanted>]) returns a string with the binary fixed point. Could also use fixp(*list, digits=<frac bits>)
  represenation of `value` to an optional amount of `digits` fractional places
- fixp2dec(value[, value, ..., digits=<fractional bits wanted>]) converts a binary fixed point string to a floating Could also use fixp2dec(*list, digits=<frac bits>)
  point representation.

Examples:
```
import fixedpoint

# Examples using single values
print(fixedpoint.approx(10.33, 4)) # Approximate 10.33 to 4 binary fraction places
print(fixedpoint.fixp(10.33))      # Print 10.33's fixedpoint representation
print(fixedpoint.fixp2dec('1010.111')) # Print floating point value for b1010.111

# Examples using lists
print(fixedpoint.approx([10.33, .2], 4)) # Approximate 10.33 to 4 binary fraction places
print(fixedpoint.fixp(*[10.33, .2]))      # Print 10.33's fixedpoint representation
print(fixedpoint.fixp2dec(*['1010.111', '1.1101'])) # Print floating point value for b1010.111

# Examples using multiple values
print(fixedpoint.fixp(10.33, .2))      # Print 10.33's fixedpoint representation
print(fixedpoint.fixp2dec('1010.111', '1.1101')) # Print floating point value for b1010.111
```

Notch Approximation GUI:
```
$ python notch_approx.py
```
Then move the slider around to remove bits from the iir filter coefficients and
see the resulting bode magnitude plot.

