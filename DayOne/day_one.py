from collections import Counter

list1 = []
list2 = []

# add values to the lists from txt file
with open("dayone_tables.txt") as f:
    for line in f:
        item1,item2 = map(int,line.split())
        list1.append(item1)
        list2.append(item2)

# Sort lists asc 
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# Count the diffs between the elements in the same position in the lists
diffs = [abs(a - b) for a, b in zip(sorted_list1, sorted_list2)]

sum_diffs = sum(diffs)
print("The sum of all the diffs is", sum_diffs)

# the answer I've gotten is 2086478 and it was correct.

#part two of the challenge is to see how often a number represented in the other list.

# Count of all the occurrences of numbers in list2
occurrences = Counter(list2)

# Calc num from list 1* occurence of every number in list 2 
result = {number: number * occurrences[number] for number in list1}

# The sum of the similarity score
similarity_score = sum(result.values())

#the answer
print(f"Total sum is {similarity_score}")