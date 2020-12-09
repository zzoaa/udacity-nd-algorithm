"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


completed_target_numbers = set()

for text in texts:
    completed_target_numbers.add(text[0])
    completed_target_numbers.add(text[1])

target_numbers = []

for call in calls:

    if call[0][0:3] == '140':
        target_numbers.append(call[1])
    else:
        completed_target_numbers.add(call[0])

possible_telemarketers = set()

for target_number in target_numbers:
    if target_number not in completed_target_numbers:
        possible_telemarketers.add(target_number)

print("These numbers could be telemarketers: ")
for call in sorted(list(possible_telemarketers)):
    print(call)
