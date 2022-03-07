def is_palindrome(word):
    new_word = word[::-1]
    for i in range(0, len(word)):
        if word[i] != new_word[i]:
            return False
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))