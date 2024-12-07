import pathlib
from itertools import product

with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as file:
    content = file.read()

valid_sums = []

def evaluate_expression(operators, numbers):
    result = numbers[0]
    for op, num in zip(operators, numbers[1:]):
        if op == "+":
            result += num
        elif op == "*":
            result *= num
    return result

for line in content.splitlines():
    if not line.strip(): 
        continue
    try:
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))
    except ValueError:
        print(f"Felaktig rad: {line}")
        continue

    operators_combinations = product(["+", "*"], repeat=len(numbers)-1)
    for ops in operators_combinations:
        if evaluate_expression(ops, numbers) == target:
            valid_sums.append(target)  
            break  

print(f"The sum of true equations: {sum(valid_sums)}")

# The answer I've gotten is 1620690235709 and it was correct.