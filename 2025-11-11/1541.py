a = input().split("-")
nums = []
for i in a:
    b = map(int, i.split("+"))
    nums.append(sum(b))
result = nums[0]
for j in range(1, len(nums)):
    result -= nums[j]

print(result)