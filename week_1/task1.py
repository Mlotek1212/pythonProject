# -*- coding: utf-8 -*-
"""
* Assignment: About EntryTest ToListDict
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Define result: list[dict]:
    2. Convert DATA from list[tuple] to list[dict]
        a. key - name from the header
        b. value - numerical value or species name
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj result: list[dict]:
    2. Przekonwertuj DATA z list[tuple] do list[dict]
        a. klucz - nazwa z nagłówka
        b. wartość - wartość numeryczna lub nazwa gatunku
    3. Uruchom doctesty - wszystkie muszą się powieść

list(
    dict(),
    dict(),
    dict(),
)
    [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
     {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
     {'Sepal length': 6.4, 'Sepal width': 3.2, 'Petal length': 4.5, 'Petal width': 1.5, 'Species': 'versicolor'},
     {'Sepal length': 4.7, 'Sepal width': 3.2, 'Petal length': 1.3, 'Petal width': 0.2, 'Species': 'setosa'}
     {'Sepal length': 4.7, 'Sepal width': 3.2}
     ]
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa')]


# Convert DATA from list[tuple] to list[dict]

def get_dict_from_list_1(row):
    _result_dict = {}
    i = 0
    for value in row:
        _result_dict[header[i]] = row[i]
        i += 1
    return _result_dict


def get_dict_from_list_2(row):
    _result_dict = {}
    i = 0
    for value in row:
        _result_dict[header[i]] = value
        i += 1
    return _result_dict


def get_dict_from_list_3(row):
    _result_dict = {}
    for i, value in enumerate(row):
        _result_dict[header[i]] = value
    return _result_dict

# list1 = ['a', 'b', 'c']
# list2 = [1,2,3]
# assert zip(list1, list2) == [('a', 1), ('b', 2), ('c', 3)]


def get_dict_from_list_4(row):
    return {key: value for key, value in zip(header, row)}


header = DATA[0]
values = DATA[1:]
# results1 = []
# results2 = []
# results3 = []
results4 = []
for row in values:
    # results1.append(get_dict_from_list_1(row))
    # results2.append(get_dict_from_list_2(row))
    # results3.append(get_dict_from_list_3(row))
    results4.append(get_dict_from_list_4(row))

results = [get_dict_from_list_4(row) for row in values]

# print("results1", results1)
# print("results2", results2)
# print("results3", results3)
# print("results4", results4)
print("results", results)
