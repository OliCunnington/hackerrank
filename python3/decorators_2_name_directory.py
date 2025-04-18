import operator


def person_lister(f):
    def inner(people):
        res = []
        #sorted(data, key=lambda x: int(itemgetter(0)(x)))
        people.sort(key=lambda x: int(operator.itemgetter(2)(x)))
        for p in people:
            res.append(f(p))
        return res
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')