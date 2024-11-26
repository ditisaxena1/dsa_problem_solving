"""
Given an array A containing n integers. The task is to check whether the array is Monotonic or not.
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].

An array A is monotone decreasing if for all i <= j, A[i] >= A[j].


"""

def if_monotonic_array(array):

    acs_arr = sorted(array)
    desc_arr = sorted(array, reverse=True)

    if acs_arr == array or desc_arr == array:
        return True, "It is a monotonic array"
    else:
        return False, "It is not a monotonic array"

print(if_monotonic_array([1,2,3,0]))


def isMonotonicArray(array):
    return (all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or
            all(array[i] >= array[i + 1] for i in range(len(array) - 1)))

print(isMonotonicArray([1,2,3,4,5]))
