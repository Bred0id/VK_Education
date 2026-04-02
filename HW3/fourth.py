def extraLetter(a, b):
    hashMapB = {}
    for ch in b:
        hashMapB[ch] = hashMapB.get(ch, 0) + 1
    for ch in a:
        if ch in hashMapB:
            hashMapB[ch] -= 1
    for letter, count in hashMapB.items():
        if count > 0:
            return letter
    return ""