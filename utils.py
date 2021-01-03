import math


def bisection(target_value):
    lo = -2
    hi = 2
    tolerance = 1e-8

    while abs(hi - lo) > tolerance:
        midpoint = lo + (hi - lo) / 2

        if math.tanh(midpoint) < target_value:
            lo = midpoint
        else:
            hi = midpoint

    return lo


def lower_bound(array, search_key):
    """
    bound
        given
            a[i] = [1,1,2,3,5,8,13,21,34]
            i    =  0 1 2 3 4 5  6  7  8
        lower bound
            you have an array and a search key
            find the index of the smallest element that's >= a value
            the value need not be in your array
            can be thought of as
                first equal to or greater than

            look for index of value 7
                index of the smallest value >= 7
                index 5
                A[i]=8

            look for index of value 8
                index of the smallest value >= 8
                also index 5
    """
    lo = 0
    hi = len(array)

    while lo < hi:
        middle = lo + (hi - lo) // 2

        if array[middle] < search_key:
            lo = middle + 1
        else:
            hi = middle

    return lo


array = [1, 1, 2, 3, 5, 8, 13, 21, 34]
# index = 0  1  2  3  4  5   6   7   8   9
