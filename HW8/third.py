def find_max_length(nums):
    prefix_sum = 0
    max_len = 0
    first_occurrence = {0: -1}
    for i, num in enumerate(nums):
        prefix_sum += (1 if num == 1 else -1)
        if prefix_sum in first_occurrence:
            length = i - first_occurrence[prefix_sum]
            if length > max_len:
                max_len = length
        else:
            first_occurrence[prefix_sum] = i
    return max_len