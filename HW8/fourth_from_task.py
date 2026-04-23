# Тут не задачка с семинара, а какая-то другая в задании, поэтому будет 2 файла на задачу 4.
def find_rotation_point(nums):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left