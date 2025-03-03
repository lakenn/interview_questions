'''


    A,                  C,         G,           T           <- curr_level
AA, AC, AG, AT,      CA ....CT                      TT      <- next_level

while working on the curr_level, prepare the next level candidates
and once all curr_level element is printed, swap next_level as curr_level , and reset next_level
'''

def dna_codes_optimal():
    choices = ['A', 'C', 'G', 'T']
    arr = choices.copy()

    # Start with level 1 (which are the single characters)
    while arr:
        code = arr.pop(0)
        yield code
        for choice in choices:
            arr.append(code + choice)



def dna_codes():

    choices = ['A', 'C', 'G', 'T']
    curr_level = choices

    while 1:
        next_level = []
        for code in curr_level:
            yield code
            for choice in choices:
                new_code = code + choice
                next_level.append(new_code)

        curr_level = next_level


a = dna_codes()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

