# main loop
if __name__=='__main__':
    digits = []
    products = []
    adjacent_nums = 13

    # open file and extract integers into list of single digits
    with open ('input.txt') as file:
        integers = file.readlines()

        for lines in range(0, len(integers)):
            for a in integers[lines]:
                digits.append(a)
            digits = digits[:-1]

        file.close()

    # start at first digit, check for zeroes within 13 digits
    for n in range(0, len(digits)):
        # start at 1,
        sum = 1

        for check in range(n, (n + adjacent_nums)):
            # if a zero is found, jump to the digit immediately after
            if int(digits[check]) == 0:
                break

            sum *= int(digits[check])

            # if a series is 'clean', calculate product and add to list
            if(check == (n + (adjacent_nums - 1))):
                products.append(sum)

    # return largest value
    print(max(products))
