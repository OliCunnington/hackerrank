

# Complete the solve function below.
def solve(s):
    cap = ""
    s = s.split()
    for w in s:
        cap = cap + w[0].upper() + w[1::] + " "
    return cap.strip()
    
