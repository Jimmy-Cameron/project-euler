def SumOfSquare(input):
    sum = 0
    while input > 0:
        sum += pow(input, 2)
        input -= 1
    return sum

def SquareOfSum(input):
    sum = 0
    while input > 0:
        sum += input
        input -= 1
    return pow(sum, 2)

# main
num = input("Input: ")
diff = SquareOfSum(int(num)) - SumOfSquare(int(num))
print(diff)
