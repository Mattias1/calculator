#
#  Calculator
# ============
#
# A quick commandline calculator.
#
import sys
from Tkinter import Tk

# Evaluate the expression
s = ''.join(sys.argv[1:]) or raw_input('> ')
if s:
    result = str(eval(s))

    # Print it
    print(result)

    # Copy it to clipboard (doesn't work in python 3, so we use python 2)
    root = Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(result)
    root.destroy()
