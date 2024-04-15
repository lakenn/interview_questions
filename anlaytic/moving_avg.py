mylist = [1, 2, 3, 4, 5, 6, 7]
N = 3

cumsum, moving_avg = [0], []

for i, x in enumerate(mylist, 1):
    cumsum.append(cumsum[i-1] + x)
    if i>= N:
        ma = (cumsum[i] - cumsum[i-N])/N
        moving_avg.append(ma)

import numpy as np

'''
The running mean is a case of the mathematical operation of convolution. 
For the running mean, you slide a window along the input and compute the mean of the window's contents. 
For discrete 1D signals, convolution is the same thing, except instead of the mean you compute an arbitrary linear combination, i.e. multiply each element by a corresponding coefficient and add up the results. Those coefficients, one for each position in the window, are sometimes called the convolution kernel. Now, the arithmetic mean of N values is (x_1 + x_2 + ... + x_N) / N, so the corresponding kernel is (1/N, 1/N, ..., 1/N), and that's exactly what we get by using np.ones((N,))/N.
'''
'''
The mode argument of np.convolve specifies how to handle the edges. I chose the valid mode here because I think that's how most people expect the running mean to work, but you may have other priorities. Here is a plot that illustrates the difference between the modes:
'''
prices = [1, 2, 3, 4, 5, 6, 7]
npPrice = np.array(prices, dtype=float)
result = np.convolve(npPrice, np.ones((3,))/3, mode='valid')
print(1)

def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / float(N)

running_mean(prices, 3)


def cumsum(prices):
    cumsum = [0]
    for i, price in enumerate(prices, 1):
        cumsum[i] = cumsum[i-1] + price
    return cumsum

print(cumsum([1,2,3,4]))

np.diff