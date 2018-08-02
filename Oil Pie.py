from fractions import Fraction

def divide_pie(groups):

    number_of_drones = sum(map(abs, groups))
    pie = Fraction(1, 1)

    for group in groups:
        f = Fraction(abs(group),number_of_drones)
        pie -= (f if group>0 else pie*f)

    return (pie.numerator, pie.denominator)