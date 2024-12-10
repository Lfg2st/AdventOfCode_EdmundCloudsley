"""Solution to day 7 part 2 of Advent of Code (AOC)."""

# Import necessary libraries
import os
import itertools
import re
import time

ROOT_DIR = "AdventOfCode_EdmundCloudsley/day_7"


start_time = time.time()
# Read input data from file
with open(os.path.join(ROOT_DIR, 'input.txt'), 'r') as f:
    txt = f.read().splitlines()


def tokeniser(expression):
    """
    Tokenize the input string expression into numbers and operators.

    Args:
        expression (str): The mathematical expression to be tokenized.

    Returns:
        list: A list of tokens, where each token is either a number or an operator.
    """
    pattern = r'\d+|[+\-*/%^|]'  # Updated pattern to include the '|' operator
    tokens = re.findall(pattern, expression) 

    return tokens


def extract(txt): 
    """
    Extract relevant data from the input text file into a structured 2D list.

    Args:
        txt (list): A list of strings, where each string is a line of the input file.

    Returns:
        list: A 2D list where each entry is a list, with the first element being the target variable 
              and the rest of the elements being the variables used to calculate it.
    """
    output = []

    for line in txt:
        line_list = line.split() 
        target = line[0:line.index(":")]
        line_list[0] = target 
        output.append(line_list)  

    return output


def non_bodmas_evaluator(expression):
    """
    Evaluate a mathematical expression from left to right, ignoring BODMAS rules.
    Supports addition, multiplication, and concatenation of numbers using the '|' operator.

    Args:
        expression (str): The mathematical expression to be evaluated.

    Returns:
        int: The result of evaluating the expression without considering BODMAS.
    """
    output = int(tokeniser(expression)[0])

    for index, token in enumerate(tokeniser(expression)):
        if token.isdigit():  
            continue

        if token == "+":
            output += int(tokeniser(expression)[index + 1])  

        elif token == "*":
            output *= int(tokeniser(expression)[index + 1])  

        elif token == "|":
            # Concatenate numbers when '|' operator is encountered
            output = int(str(output) + tokeniser(expression)[index + 1])  
    return output


from tqdm import tqdm

def main():
    """
    Main function to process input data and evaluate expressions.
    Extracts the matrix, generates permutations of operators, evaluates expressions 
    ignoring BODMAS, and accumulates the result if the evaluation matches the target.
    """
    matrix = extract(txt=txt)
    operators = ['+', '*', '|']  # Including the '|' operator for concatenation

    total = 0
    for row in tqdm(matrix, desc="Processing Rows", unit="row"):
        target_value = int(row[0])  

        num_operators = len(row) - 2 
        operator_permutations = list(itertools.product(operators, repeat=num_operators))  

        for permutation in tqdm(operator_permutations, desc="Evaluating Expressions", unit="permutation", leave=False):
            expression = ""
            for idx in range(1, len(row)):
                expression = expression + row[idx]  
                if idx != len(row) - 1:
                    expression = expression + permutation[idx - 2]
            evaluated_result = non_bodmas_evaluator(expression)  

            if evaluated_result == target_value: 
                total += evaluated_result 
                break
    
    print(total)  
    print(time.time() - start_time) 


if __name__ == "__main__":
    main()
