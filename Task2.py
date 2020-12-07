"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
tn = {}
for call in calls:

    if call[0] in tn:
        tn[call[0]] = int(tn[call[0]]) + int(call[3])
    else:
        tn[call[0]] = int(call[3])

    if call[1] in tn:
        tn[call[1]] = int(tn[call[1]]) + int(call[3])
    else:
        tn[call[1]] = int(call[3])

answer_tn = None
answer_time = 0
for key in tn.keys():
    if answer_time < tn[key]:
        answer_time = tn[key]
        answer_tn = key

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    answer_tn, answer_time
))
