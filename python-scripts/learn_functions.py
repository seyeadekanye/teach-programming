'''Scenario 1
Imagine you are a teacher who teaches 3 classes.
Class 1: Very smart
Class 2: Medium level intellect
Class 3: Have trouble learning

State standards require all Classes take the same final exam with the same questions.
However they have set Pass/fail thresholds for each level. Where each class level matches 
the corresposnding threshold level

Threshold 1: 85
Threshold 2: 70
Theshold 3: 55
'''

# Determine the category pass/fail of each for each score based on the class

import csv

with open("../data/ClassScores.csv", 'r', newline='') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)