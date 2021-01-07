
a = [2,3,4,4,4,101]
a = [-2,-1,0,3,4,4,4,90,101]
a = [4,4,4]
a = [4,4,4,5,6]
a = [-3,-2,0,4,4,4,4,4]
2 ** 31 -1
-2 ** 32

# 升序
# 有且有仅有一组重复数字
# 开始index，
def get_repeat(nums):
    start_index, count = -1, 1
    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i]:
            if start_index == -1:
                start_index = i
            count += 1
    return start_index, count

start_index, count = get_repeat(a)
print(start_index)
print(count)

