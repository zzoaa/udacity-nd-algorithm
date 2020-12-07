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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

telephone_numbers = {}

for text in texts:
    telephone_numbers[text[0]] = 0
    telephone_numbers[text[1]] = 0

for call in calls:
    telephone_numbers[call[0]] = 0
    telephone_numbers[call[1]] = 0

num_of_t = len(telephone_numbers.keys())
print("There are {} different telephone numbers in the records.".format(
    num_of_t))
