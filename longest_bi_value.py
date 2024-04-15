import pandas as pd
import numpy as np

def class_grades(students):
    """
    :param students: (list) Each element of the list is another list with the
      following elements: Student name (string), class name (string), student grade (int).
    :returns: (list) Each element is a list with the following
      elements: Class name (string), median grade for students in the class (float).
    """
    df = pd.Dataframe(students, columns=['name', 'class_name', 'score'])
    df.groupby(['class_name']).median()
    return df.values.tolist()

students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
print(class_grades(students))

from collections import Counter


def find_unique_numbers(numbers):
    number_count = Counter(numbers)

    result = [x for x, count in number_count.items() if count == 1]
    return result


print(find_unique_numbers([1, 2, 1, 3]))


from enum import Enum

class Side(Enum):
    none = 0
    left = 1
    right = 2

class ChainLink:

    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception('Link already connected!')
        self._right = link
        link._left = self

    def longer_side(self):
        return None

left = ChainLink()
middle = ChainLink()
right = ChainLink()
left.append(middle)
middle.append(right)
print(left.longer_side() == Side.right)

from enum import Enum


class Side(Enum):
    none = 0
    left = 1
    right = 2


class ChainLink:
    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception('Link already connected!')
        self._right = link
        link._left = self

    def longer_side(self):
        right_count = 0
        left_count = 0

        temp = self._right

        while (temp != None and temp != self):
            temp = temp._right
            right_count += 1

        temp = self._left
        while (temp != None and temp != self):
            temp = temp._left
            left_count += 1

        if left_count == right_count:
            return Side.none
        elif left_count < right_count:
            return Side.right

        return Side.left


left = ChainLink()
middle = ChainLink()
right = ChainLink()
left.append(middle)
middle.append(right)
print(left.longer_side() == Side.right)


class MovingTotal:
    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        pass

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return None


if __name__ == "__main__":
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    movingtotal.append([4])
    print(movingtotal.contains(9))


from typing import Dict, Tuple, Callable, Iterable

import numpy

def model_quadratic(model_parameters: dict):
    """
    This is a quadratic model with a minimum at a=0.5, b=0.75, c=0.25.
    """
    a = model_parameters['a']
    b = model_parameters['b']
    c = model_parameters['c']

    return 1.75 + (a - 0.5) ** 2 + (b - 0.75) ** 2 + (c - 0.25) ** 2


class Problem:
    @staticmethod
    def grid_search(search_space: Dict[str, Iterable],
                    scoring_func: Callable[[Dict[str, float]], float]) -> Tuple[float, Dict[str, float]]:
        """
        This function accepts a search space, which is a dictionary of arrays.

        For each key in the dictionary, the respective array holds the numbers in the search space that should be
        tested for.

        This function also accepts a scoring_func, which is a scoring function which will return a float score given a
        certain set of parameters.  The set of parameters is given as a simple dictionary. As an example, see
        model_quadratic above.
        """

        return 1.75, {'a': 0.5, 'b': 0.75, 'c': 0.25}


print(Problem.grid_search({
    'a': numpy.arange(0.0, 1.0, 0.05),
    'b': numpy.arange(0.0, 1.0, 0.05),
    'c': numpy.arange(0.0, 1.0, 0.05),
}, model_quadratic))

from collections import Counter


def nth_most_rare(elements, n):
    """
    :param elements: (list) List of integers.
    :param n: (int) The n-th element function should return.
    :returns: (int) The n-th most rare element in the elements list.
    """
    element_count = dict(Counter(elements))
    return sorted(element_count, key=element_count.get)[n - 1]


print(nth_most_rare([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))

import pandas as pd

products = {'Product': ['Tablet','iPhone','Laptop','Monitor'],
            'Price': [250,800,1200,300]
            }

df = pd.DataFrame(products, columns= ['Product', 'Price'])

products_list = df.values.tolist()
print (products_list)

from collections import Counter


def nth_most_rare(elements, n):
    """
    :param elements: (list) List of integers.
    :param n: (int) The n-th element function should return.
    :returns: (int) The n-th most rare element in the elements list.
    """
    element_count = dict(Counter(elements))
    return sorted(element_count, key=element_count.get)[n]


print(nth_most_rare([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))