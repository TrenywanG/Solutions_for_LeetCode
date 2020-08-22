nums = [2, 7, 11, 15]
target = 9


def twosum(nums, target):
    output = []
    for i, num_i in enumerate(nums):
        if target - num_i in nums and i != nums.index(target - num_i):
            output.extend((i, nums.index(target - num_i)))
        return output

print(twosum(nums, target))
