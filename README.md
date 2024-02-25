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
- approx(value, digits) rounds `value` to `digits` bit fractional places
- fixp(value[, digits]) returns a string with the binary fixed point
  represenation of `value` to an optional amount of `digits` fractional places
- fixp2dec(value[, digits]) converts a binary fixed point string to a floating
  point representation.

Examples:
```
import fixedpoint

print(approx(10.33, 4)) # Approximate 10.33 to 4 binary fraction places
print(fixp(10.33))      # Print 10.33's fixedpoint representation
print(fixp2dec('1010.111')) # Print floating point value for b1010.111
```

Notch Approximation GUI:
```
$ python notch_approx.py
```
Then move the slider around to remove bits from the iir filter coefficients and
see the resulting bode magnitude plot.

