
# combination
import itertools

somelist = [
    [1,2,3],
    [4,5]
]

for element in itertools.product(*somelist):
    print(element)

# permutations
list1 = ["a", "b", "c"]
list2 = [1, 2]
all_combinations = []

list1_permutations = list(itertools.permutations(list1, len(list2)))
print(list1_permutations)


def look_say(number):
  number_str = str(number)
  result = ''.join(str(len(list(g))) + k for k, g in groupby(number_str))
  return int(result)

print(look_say(12))