# migrated from python 2.7
from datetime import date

def checkio(from_date, to_date):
    return len([c for c in [(i+from_date.weekday()) % 7 for i in range((to_date - from_date).days + 1)] if c==5 or c==6])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"