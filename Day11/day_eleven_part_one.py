"""
Rules:
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.

If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
(The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

If none of the other rules apply, the stone is replaced by a new stone; 
the old stone's number multiplied by 2024 is engraved on the new stone.
"""

import pathlib

with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as file:
    for line in file:
        stones = [int(x) for x in line.strip().split()]

def change_stones(stones):
    next_batch_of_stones = []
    for stone in stones:
        if stone == 0:
            next_batch_of_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            next_batch_of_stones.append(int(stone[:len(stone)//2]))
            next_batch_of_stones.append(int(stone[len(stone)//2:]))
        else:
            next_batch_of_stones.append(stone * 2024)
    return next_batch_of_stones

print(change_stones(stones))
new_stones = stones

i = 0
while i < 25:
    new_stones = change_stones(new_stones)
    i += 1

count = len(new_stones)

print(f"The number of stones after blinking 25 times is {count}")

# Answer: 186424