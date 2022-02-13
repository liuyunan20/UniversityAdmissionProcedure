nums = [int(num) for num in list(input())]
sorted_nums = sorted(nums, key=lambda x: x % 3)
print(sorted_nums)
# write your code here
