"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

Examples:
csReverseIntegerBits(417) -> 267
417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
csReverseIntegerBits(267) -> 417
csReverseIntegerBits(0) -> 0

Notes:
The input integer will not be negative.
[execution time limit] 4 seconds (py3)
[input] integer n
[output] integer
"""

def csReverseIntegerBits(n):
    x = bin(n).replace("0b", "")
    
    x = list(x)
    x.reverse()
    x = "".join(x)

    x = int(x, 2)
    return x

print(csReverseIntegerBits(417))
print(csReverseIntegerBits(267))
print(csReverseIntegerBits(0))