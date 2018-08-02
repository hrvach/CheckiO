# migrated from python 2.7
from fractions import gcd
from functools import reduce

greatest_common_divisor = lambda *args: reduce(gcd, args)