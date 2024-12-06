"""Solution to question 1/part 2 of Advent Of Code. See https://adventofcode.com/2024/day/1"""

#Copying input value


import time

start_time = time.time()


with open('day_1/day1.txt', 'r') as f:
    txt = f.read().splitlines()

list_1 = []
list_2 = []

for line in txt:
    list_1.append(int(line[0:5]))
    list_2.append(int(line[8:13]))

def find_repetitions(target, list):
    n_repetitions = 0
    for index in range(len(list)):
        if list[index] == target:
            n_repetitions += 1
    return n_repetitions

def similarity_score(list_1, list_2):
    score = 0
    for index_l1 in range(len(list_1)):
        score = score + list_1[index_l1]*find_repetitions(list_1[index_l1], list_2)
    return score


total_time = time.time() - start_time
print(similarity_score(list_1, list_2), total_time)