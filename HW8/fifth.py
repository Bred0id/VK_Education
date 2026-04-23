def is_balanced_parentheses(s):
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
        else:
            return False
        if balance < 0:
            return False
    return balance == 0