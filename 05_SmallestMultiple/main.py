def smallest_multiple(multiple):
    # must be at least a multiple of 20 - check if all numbers go into
    # multiples of 20, break when it doesn't and go to next multiple of 20
    num = multiple

    while True: # dangerous - think of a better way of doing this
        div = multiple
        num += multiple

        # don't need to check, if it ends in 0 it will always be divisible by 1 and 2
        while div > 0:
            if num % div == 0:
                div -= 1
            else:
                break

        if div == 0:
            return num

# main loop
max_multiple = input("Enter the highest number to be divisible by: ")
print(smallest_multiple(int(max_multiple)))
