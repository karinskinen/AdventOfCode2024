"""
Day 3 problem:

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. 
All of the instructions have been jumbled up.
It seems like the goal of the program is just to multiply some numbers. 
It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. 
There are many invalid characters that should be ignored, even if they look like part of a mul instruction. 
Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. 
Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. 
What do you get if you add up all of the results of the multiplications?
"""

import pathlib
import re

with open(f"{pathlib.Path(__file__).parent.resolve()}/day_three_input.txt", "r") as file:
    content = file.read()

pattern = r"(?<!\w)mul\((\d{1,3}),\s*(\d{1,3})\)"
matches = re.findall(pattern, content)

total_sum = 0

for match in matches:
    x, y = int(match[0]), int(match[1])  
    total_sum += x * y  


print(f"The total sum is: {total_sum}")

#the correct answer in my case is 163931492

"""
PART TWO:

As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact.
If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:
- The do() instruction enables future mul instructions.
- The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) 
instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, 
including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""
import pathlib
import re

enabled = True
total_sum = 0

with open(f"{pathlib.Path(__file__).parent.resolve()}/day_three_input.txt", "r") as file:
    content = file.read()

pattern = r"(?<!\w)mul\((\d{1,3}),\s*(\d{1,3})\)|(?<!\w)do\(\)|(?<!\w)don't\(\)"
matches = re.finditer(pattern, content)

for match in matches:
    if match.group(1) and match.group(2):  
        if enabled:
            x, y = int(match.group(1)), int(match.group(2)) 
            total_sum += x * y
    elif match.group() == "do()":  
        enabled = True
    elif match.group() == "don't()":  
        enabled = False

print(f"The total sum is: {total_sum}")

#the correct answer was 76911921 



