# migrated from python 2.7
from itertools import *

color = ['blue', 'green', 'red', 'white', 'yellow']
pet = ['cat', 'bird', 'dog', 'fish', 'horse']
beverage = ['beer', 'coffee', 'milk', 'tea', 'water']
cigarettes = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
nationality = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
number = ['1', '2', '3', '4', '5']


def answer(relations, question):
    possible = list(map(set, product(color, pet, beverage, cigarettes, nationality, number)))
    constraints = [set(i.split('-')) for i in relations]
    where, what = question.split('-')
    possible = [p for p in possible if not any([len(i&p;)%2 for i in constraints])
                      and where in p]
    return (set(eval(what)) & possible[0]).pop()