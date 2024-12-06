


"""Solution to question 1/part 1 of Advent Of Code. See https://adventofcode.com/2024/day/1"""

#Copying input value

with open('day_1/day1.txt', 'r') as f:
    txt = f.read().splitlines()

list_1 = []
list_2 = []

for line in txt:
    list_1.append(int(line[0:5]))
    list_2.append(int(line[8:13]))



import time
start_time = time.time()



# sorting the two lists
def sort(list_i):
    for counter in range(len(list_i)):
        switched = False

        for index in range(len(list_i)-1):
            if list_i[index] > list_i[index + 1]:
                list_i[index], list_i[index + 1] = list_i[index + 1], list_i[index]

                switched = True
        if switched == False:
            break
    return list_i


def compute_distances(list_1, list_2): 
    # assumes the lists are already sorted
    distance = 0
    for index in range(len(list_1)):
        distance = distance + abs(list_1[index] - list_2[index])

    return distance

def main(list_1, list_2):
    print(compute_distances(sort(list_1), sort(list_2)))


main(list_1, list_2)

print(time.time() - start_time)





