#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    
    # # generate list of pairs / teams
    # teams = [(x, y) for x in topic for y in topic if x != y and topic.index(x) < topic.index(y)]
    # # this gives a list of tupples, that contain the known subjects string of both team members
    # # [([],[]), ...]
    
    # teams_merged = []
    # # merge teams lists
    # for team in teams:
    #     _team = []
    #     # team is tupple of string
    #     for i in range(len(team[0])):
    #         _team.append(1) if (team[0][i] == "1" or team[1][i] == "1") else _team.append(0)
    #     teams_merged.append(_team)
    # # teams_merged now contains list of (int) for each known subject
    
    # # count known subjects per team
    # teams_known = [x.count(1) for x in teams_merged]
    
    # # return [max value, count of max value] in teams_known
    # return [max(teams_known), teams_known.count(max(teams_known))]
    
    looped_team = []
    ### for looped
    # since .index and .count are probably not great
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            _team = 0
            for k in range(len(topic[i])):
                if (topic[i][k] == "1" or topic[j][k] == "1"):
                    _team += 1
            looped_team.append(_team)
        return [max(looped_team), looped_team.count(max(looped_team))]            
                
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
