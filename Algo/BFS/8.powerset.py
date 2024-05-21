def powerSetPickAlgo(some_list):
    def power_set(index, curr):
        if len(some_list) == index:
            print(curr)
            return

        power_set(index+1, curr + [some_list[index]])
        power_set(index+1, curr)

    power_set(0, [])

powerSetPickAlgo(['a', 'b', 'c'])
