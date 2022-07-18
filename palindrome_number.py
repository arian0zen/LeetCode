from tkinter import N


def isPalindrome(x):
    x = str(x)
    s = 0
    e = len(x)-1
    while s <= e:
        if x[s] == x[e]:
            s += 1
            e -= 1
        else:
            return False
    return True

number = 12321
print(isPalindrome(number))

        