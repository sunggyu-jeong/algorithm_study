nums = [int(input()) for _ in range(9)];
maxValue = max(nums);
print(maxValue)
print(nums.index(maxValue) + 1);