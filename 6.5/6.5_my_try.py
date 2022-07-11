# too easy!

def palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[~i]:
            return False
    return True


# This is *ACTUALLY* the right answer, removes alphanumerics
def palindrome_with_alhpanum(s):
    left = 0
    right = len(s) - 1

    while left < right:
        print(left, right)
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                print(left, right)
                return False
        elif ~s[right].isalnum():
            right -= 1
        elif ~s[left].isalnum():
            left += 1

    return True



