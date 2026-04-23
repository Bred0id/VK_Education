# А вот тут задачка с семинара)
def pivot_index(nums):
    total_sum = 0
    left_sum = 0
    for num in nums:
        total_sum += num
    for i in range(len(nums)):
        if left_sum == total_sum - left_sum - nums[i]:
            return i
        left_sum += nums[i]
    return -1