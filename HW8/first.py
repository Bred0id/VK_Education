def max_sum_subarray_k(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum