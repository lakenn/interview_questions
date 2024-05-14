# https://www.efinancialcareers.com/news/2020/06/python-interview-questions-hedge-fund
# https://anywhere.epam.com/en/blog/senior-python-developer-interview-questions
# https://anywhere.epam.com/en/blog/python-interview-questions
from collections import namedtuple

a = b = [1]
a += [2]
print (b)
a = a + [3]
print (b)

multipliers = [lambda x, i=i: (i+1)*x for i in range(5)]


Grade = namedtuple('Grade', ('score', 'weight'))
Grade(10, 20)
print(Grade(10, 20))