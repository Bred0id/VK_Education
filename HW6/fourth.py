def longest_palindrome(s):
    if not s:
        return ""

    start = 0
    max_len = 1

    def expand_center(left, right):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                start = left
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_center(i, i)
        expand_center(i, i + 1)

    return s[start:start + max_len]