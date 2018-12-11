def largest_cont_sum(input):
    cumsum = 0
    max_value = 0

    for elem in input:
        cumsum += elem

        # if cumsum is smaller than zero
        if cumsum < 0:
            # meaning dun take the elem
            cumsum = 0

        if max_value < cumsum:
            max_value = cumsum


    return max_value

