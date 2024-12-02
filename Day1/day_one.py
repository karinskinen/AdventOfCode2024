from collections import Counter

list1 = []
list2 = []

with open("dayone_tables.txt") as f:
    for line in f:
        item1,item2 = map(int,line.split())
        list1.append(item1)
        list2.append(item2)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

diffs = [abs(a - b) for a, b in zip(sorted_list1, sorted_list2)]

sum_diffs = sum(diffs)
print("The sum of all the diffs is", sum_diffs)

# the answer I've gotten is 2086478 and it was correct.

occurrences = Counter(list2)

result = {number: number * occurrences[number] for number in list1}

similarity_score = sum(result.values())

print(f"Total sum is {similarity_score}")