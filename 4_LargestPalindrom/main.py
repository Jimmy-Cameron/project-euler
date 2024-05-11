def largest_palindrome():
    flipped_num = 0
    palindromes = []

    for a in range(100,999):
        for b in range(100,999):
            # perform calculation
            c = a * b
            flipping = c
            flipped_num = 0

            # reverse answer
            while flipping > 0:
                remainder = flipping % 10
                flipped_num = (flipped_num * 10) + remainder
                flipping = flipping // 10

            # check if equal
            if c == flipped_num:
                palindromes.append(flipped_num)

    return palindromes

# main loop
ans = largest_palindrome()
print("Biggest = ", max(ans))

# a = 10
# b = 15
# flipped_num = 0
# c = a * b
# flipping = c
# flipped_num = 0
#
# # reverse answer
# while flipping > 0:
#     remainder = flipping % 10
#     flipped_num = (flipped_num * 10) + remainder
#     flipping = flipping // 10
#
# print(c)
# print(flipped_num)
