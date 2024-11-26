""""

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

"""


def running_sum(nums: list[int]) -> list[int]:
    new_array = []
    run_sum = 0
    for i in range(len(nums)):
        # sum1 = 0
    #     for j in range(0, i+1): // using 2 loops is more time complex. 
    #         sum1 += nums[j]
    #     new_array.append(sum1)
    # return new_array
        run_sum += nums[i]
        new_array.append(run_sum)
    return new_array


print(running_sum(nums=[1,2,3,4]))


