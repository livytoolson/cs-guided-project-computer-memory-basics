"""
Convert string to uppercase without using the built in .upper() Python function

This will show us how the computer represents these characters because characters are made of binaries

Need to map numbers to memory

ASCII - American Standard Code for Information Interchange
 - has some limitations
 - only has 7 bits
 - can only store 128 characters with it

Unicode - character mapping 
 - has over 1 million characters defined
 - Unicode defines a number for every single character
 - Unicode is the same as ASCII for the first 128 characters

UTF-8 - most popular encoding in the world
 - takes a number and represents it as a sequence of bits
 - UTF-8 is the same as ASCII for the first 128 characters

A = 65
a = 97

97 - 65 = 32 
The alphabet increases sequentially - we see that the difference between the two is 32
"""

a = "Hi There!"

# determines if the character is alphabetic or not -->
# return true or false depending on if something is lowercase or not
# ord gives us the unicode code point value
def my_islower(c):
    cp = ord(c)
    
    return 97 <= cp <= 122
    # return (cp >= 97 and cp <= 122)
    """
    This can be rewritten in a simpler form -- see above
    If you are returning if one thing return True, else return False you can always use the simplier version
    if cp >= 97 and cp <= 122:
        return True 

    else:
        return false
    """

# print(my_islower('a'))
# print(my_islower('z'))
# print(my_islower('A'))
# print(my_islower('Z'))
# print(my_islower('!'))
# print(my_islower('~'))
# print(my_islower(' '))

# we only want to uppercase alphabetic characters
def my_upper(s):
    result = ''

    # send every character to my_islower
    for c in s:

    # if char is lowercase
        if my_islower(c):

            # get the ord value
            vale = ord(c)

            # subtract 32
            val -= 32

            # convert value back to character - chr is oppositve of ord (takes value and turns it into a character)
            c = chr(val)

            # add to result
            reslt += c
        
        else:
            result += c

    # return result
    return result

print(my_upper(a))