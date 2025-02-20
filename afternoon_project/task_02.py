"""
Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII table.

Examples:
csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
01101100 -> 108 -> "l"
01100001 -> 97 -> "a"
01101101 -> 109 -> "m"
01100010 -> 98 -> "b"
01100100 -> 100 -> "d"
01100001 -> 97 -> "a"
csBinaryToASCII("") -> ""

Notes:
The input string will always be a valid binary string.
Characters can be in the range from "00000000" to "11111111" (inclusive).
In the case of an empty input string, your function should return an empty string.
[execution time limit] 4 seconds (py3)
[input] string binary
[output] string
"""

import re

def csBinaryToASCII(binary):
    res = ''
    x = re.findall('.{1,8}', binary)

    for s in x:
       y = chr(int(s,2))
       res += y

    return res

print(csBinaryToASCII("011011000110000101101101011000100110010001100001"))
print(csBinaryToASCII(""))