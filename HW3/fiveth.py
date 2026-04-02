def twoSum(data, target):
    cache = {}
    for i in range(len(data)):
        cache[data[i]] = i
    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache and cache[diff] != i:
            return [i, cache[diff]]
    return []