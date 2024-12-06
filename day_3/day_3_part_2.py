import re
import time
start_time = time.time()
def mul_evaluator(string):
    """
    Evaluates the multiplication of two numbers in the format 'mul(<number>,<number>)'.
    
    Args:
        string (str): The input string of the form 'mul(<number>,<number>)'.
    
    Returns:
        int: The result of multiplying the two numbers.
        str: 'invalid' if the format is incorrect.
    """
    number_1 = ""
    number_2 = ""
    extract_number_2 = False

    for index in range(4, len(string) - 1):
        if string[index] == ",":
            extract_number_2 = True
        elif not extract_number_2:
            number_1 = number_1 + string[index]
        elif extract_number_2:
            number_2 = number_2 + string[index]
        else:
            return 'invalid'
    
    return int(number_1) * int(number_2)

def pattern_validator(string):
    """
    Validates if the input string matches the pattern 'mul(<digit>,<digit>)'.
    
    Args:
        string (str): The string to validate.
    
    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    pattern = r'^mul\(\d+,\d+\)$'

    if re.match(pattern, string):
        return True
    else:
        return False

# Data ingestion
with open('day_3/day_3_input.txt', 'r') as f:
    input = f.read()



sum =  0
evaluate_mul = True



# Iterate through the input string
for index in range(0, len(input)):


    # check for the presence of do and don't()
    if input[index] == 'd' and input[index + 1] == 'o' and input[index + 2] == '(' and input[index + 3] == ')' :
        evaluate_mul = True
    elif input[index] == 'd' and input[index + 1] == 'o' and input[index + 2] == 'n' and input[index + 3] == "'" and input[index + 4] == 't':
        evaluate_mul = False

    

    

    if evaluate_mul:
        if input[index] == "m":
            test_strings = []

            for i in range(7, 12):
                test_string = ""
                for j in range(0, i + 1):
                    try:
                        test_string = test_string + input[j + index]
                    except Exception as e:
                        pass

                test_strings.append(test_string)

            for test_string in test_strings:
                if pattern_validator(test_string):
                    sum = sum + mul_evaluator(test_string)

# Print the total sum
print(sum)
print(time.time() - start_time)
