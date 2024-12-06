import time
start_time = time.time()

with open("day_2/day_2_input.txt", "r") as f:  
    txt = f.read().splitlines()

safe_counter = 0

def check_safety(levels):
    change = 'increasing' if levels[1] - levels[0] > 0 else 'decreasing'
    safe = True  

    for i in range(len(levels) - 1):  
        difference = levels[i + 1] - levels[i]

        if not (1 <= abs(difference) <= 3):  
            safe = False  
            break

        if (change == 'increasing' and difference < 0) or (change == 'decreasing' and difference > 0):  
            safe = False  
            break

    return safe

for line in txt:  
    levels = list(map(int, line.split()))

    # Check if the report is safe without any removal
    if check_safety(levels):
        safe_counter += 1
        continue  


    found_safe_after_removal = False
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]  
        if check_safety(new_levels):  
            found_safe_after_removal = True
            break

    if found_safe_after_removal:
        safe_counter += 1

print(time.time() - start_time)
print("Number of safe reports:", safe_counter)
