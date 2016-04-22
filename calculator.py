#
#  Calculator
# ============
#
# A quick commandline calculator.
#
import sys
import random
import string
from Tkinter import Tk


def process(s):
    result = str(eval(s))
    print(result)
    return result


def copyToClipboard(s):
    # (Doesn't work in python 3, so we use python 2)
    root = Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(s)
    root.destroy()


def randomNumber(n):
    return ''.join(random.SystemRandom().choice(string.digits) for _ in range(n))


def randomString(n):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))


def main():
    s = ''.join(sys.argv[1:]) or raw_input('> ')

    predefinedFunctions = ['randomNumber', 'randomString']
    for f in predefinedFunctions:
        if s[:len(f)] == f:
            n = eval(s[len(f) + 1:])
            s = '"{}"'.format(globals()[f](n))

    if s:
        s = process(s)
        copyToClipboard(s)


main()
