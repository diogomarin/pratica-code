def find_max(nums):
    max_num = float("-inf") #smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([1,2,11,5,4,6,5,7,9,8,1]))

