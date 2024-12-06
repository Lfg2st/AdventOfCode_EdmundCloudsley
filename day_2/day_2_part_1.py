import time
start_time = time.time()

with open("day_2/day_2_input.txt", "r") as f:  
    txt = f.read().splitlines()

safe_counter = 0

for line in txt:  
    levels = list(map(int, line.split()))

    if levels[1] - levels[0] > 0:  
        change = 'increasing'  
    else:  
        change = 'decreasing'

    safe = True  

    for i in range(len(levels) - 1):  
        difference = levels[i + 1] - levels[i]

        if not (1 <= abs(difference) <= 3):  
            safe = False  
            break

        if (change == 'increasing' and difference < 0) or (change == 'decreasing' and difference > 0):  
            safe = False  
            break

    if safe:  
        safe_counter += 1
print(time.time() - start_time)
print("Number of safe reports:", safe_counter)
