i = int(input())

"""
간격
0 -> 111, 222, 333, 444, 555, 666, 777, 888, 999
1 -> 210, 321, 432, 543, 654, 765, 876, 987 (x + x - 1)
2 -> 420, 531, 642, 753, 864, 975 (x + x - 1)
3 -> 630, 741, 852, 963 (x + x - 1)
4 -> 840, 951 (x + x - 1)
"""

"""
starting point

0~99 => all

1xx -> 111 135 147 159
2xx -> 222 246 258 | 210
3xx -> 

"""

def is_valid_digit(digit_array, limit):
    number = digit_array[0] * 100 + digit_array[1] * 10 + digit_array[2]
    c1 = 0 < digit_array[0] < 10
    c2 = 0 <= digit_array[1] < 10
    c3 = 0 <= digit_array[2] < 10

    return c1 and c2 and c3 and (number <= limit)

if i < 100:
    res = i
else:
    res = 99
    for hundred_digit in range(1, 10):
        for spacing in range(0, 5):
            # positive direction
            positive_digit = [hundred_digit, hundred_digit + spacing, hundred_digit + spacing * 2]
            if is_valid_digit(positive_digit, i):
                res += 1
            if spacing != 0:
                # negative direction
                negative_digit = [hundred_digit, hundred_digit - spacing, hundred_digit- spacing * 2]
                if is_valid_digit(negative_digit, i):
                    res += 1

print(res)
