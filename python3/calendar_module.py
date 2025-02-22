import calendar


inp = input().split()
# 0 = M
# 1 = D
# 2 = Y
cal = calendar.Calendar().itermonthdays2(int(inp[2]), int(inp[0]))
d = ""
for (date, day) in cal:
    if date == int(inp[1]):
        d = calendar.day_name[day].upper()
print(d)