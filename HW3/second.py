def copyTime(n, x, y):
    l = 0
    r = (n - 1) * max(x, y)
    while l + 1 < r:
        mid = (r + l) // 2
        if mid // x + mid // y < n - 1:
            l = mid
        else:
            r = mid
    return r + min(x, y)