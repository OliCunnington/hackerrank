import re

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            if len(str(l[i])) > 10:
                l[i] = re.sub(r"^(?:0|91|\+91)", "", str(l[i]))
            l[i] = "+91 {} {}".format(str(l[i])[:5], str(l[i])[5:])
            # print(l[i])
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 