'''
import unittest
# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_should_find_the_number_appearing_odd_times(self):
    self.assertEqual(find_odd([1]), 1)
    self.assertEqual(find_odd([5,1,1,5,2,2,5]), 5)

'''

def find_odd(integers):
    result = 0

    for element in integers:
        result = result ^ element

    return result