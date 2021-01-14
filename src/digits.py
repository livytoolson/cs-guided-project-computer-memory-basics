"""
ex:
a = [1,2,3,4,5,6,7,8,9 ..., 10100101, 10100012]

x = a[3]
y = a[8]
z = a[32422]

memory location         value
---------------         -----
3566                    1           <--- a, a[0]
3567                    2           <---    a[1]
3568                    3
3569                    4           <---    a[4]
3570                    5
3571                    6

What is the address of a[4]

Take the address of a[0]: 3566
Add on the index of a[4], 4: 3566 + 4 = 3570

*********************************************************************************************************

Memory is like a big array - it has indexes and at each of those indexes you can store a value in memory

To find the address of any element add the index to the base element

Bit: "Binary Digit", 1 or 0
Byte: 8 bits, can hold values from 0-255

Binary numbering system is base 2, there are 2 digits (0 and 1)
Decimal is base 10, 10 digits: 0-9

Arrays are stored sequentially in memory. Do simple math to go where in memory to get the value out. Arrays are O(1)
"""
