

# Complete the solve function below.
def solve(s):
    temp = list(s)
    temp[0] = temp[0].upper()
    for c in range (1,len(temp)):
        if temp[c-1] == " ":
            temp[c] = temp[c].upper()
    return "".join(temp)

