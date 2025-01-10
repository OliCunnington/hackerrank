def minion_game(string):
    # your code goes here
    string = string.lower()
    results = ["Stuart", 0, "Kevin", 0]
    vowels = ["a", "e", "i", "o", "u"]
    for i in range (len(string)):
        if string[i] in vowels:
            results[3] += len(string) - i
        elif string[i] != "y":
            results[1] += len(string) - i
    if results[1] == results [3]:
        print("Draw")
    elif results[1] > results[3]:
        print("%s %d" % (results[0],results[1]))
    else:
        print("%s %d" % (results[2],results[3]))

