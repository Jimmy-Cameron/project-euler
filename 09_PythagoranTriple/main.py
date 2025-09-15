def CheckIfPythagoran(a, b, c):
    if a*a + b*b == c*c:
        return True
    else:
        #print("Not Pythag")
        False

def CheckSize(a, b, c):
    if a + b + c == 1000:
        if a < b and b < c:
            return True
        else:
            #print("Wrong order")
            return False
    else:
        return False

# main loop
if __name__=='__main__':
    for a in range(1, 998):
        for b in range((a + 1), 998):
            for c in range((b + 1), 998):
                if CheckSize(a, b, c):
                    if CheckIfPythagoran(a, b, c):
                        print(f"Product = {a*b*c}")
                        break

