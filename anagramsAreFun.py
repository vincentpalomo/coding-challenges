def areAnagrams(a, b):
    print(a, b)
    a_length = len(a)
    b_length = len(b)

    if (a_length != b_length):
        return False

    letters = [0] * 26

    for i in range(a_length):
        current_char = a[i]
        print(current_char)
        index = ord(current_char) - ord('a')
        letters[index] += 1

    print(letters, 'before removing letters array')

    for i in range(b_length):
        current_char = b[i]
        print(current_char)
        index = ord(current_char) - ord('a')
        letters[index] -= 1

    print(letters, 'after removing letters array')

    for i in range(26):
        if (letters[i] != 0):
            return False
        else:
            return True


ret = areAnagrams('hello', 'olleh')
ret2 = areAnagrams('hello', 'goodbye')

print("Anagrams" if ret == True else "Not Anagrams")
print("Anagrams" if ret2 == True else "Not Anagrams")
