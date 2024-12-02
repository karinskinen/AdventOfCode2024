import pathlib

num_of_safe_reports = 0

#are the levels asc
def is_asc(level):
    return all(level[i] < level[i+1] for i in range(len(level)-1))

#are the levels desc
def is_desc(level):
    return all(level[i] > level[i+1] for i in range(len(level)-1))

#is the difference 1, 2 or 3 between two levels next to each other
def diff_ok(level):
    return all(1 <= abs(level[i] - level[i+1]) <= 3 for i in range(len(level)-1))

#is a report safe with the regards to the rules
def is_a_report_safe(level):
    return (is_asc(level) or is_desc(level)) and diff_ok(level)

#make a report safe with the Problem Dampener
def make_an_unsafe_report_safe(level):
    for i in range(len(level)):
        new_report = level[:i] + level[i+1:] 
        if is_a_report_safe(new_report): 
            return True
    return False


#opening file to analyze every report
with open(f"{pathlib.Path(__file__).parent.resolve()}/day_two_input.txt", "r") as file:
    for reports, report in enumerate(file, start=1):
        levels = [int(x) for x in report.strip().split()]
        #is a report safe?
        if is_a_report_safe(levels) or make_an_unsafe_report_safe(levels):
            num_of_safe_reports +=1
    
print(f"There are {num_of_safe_reports} safe reports ")

