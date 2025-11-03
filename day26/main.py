import random

import pandas
from numpy.ma.core import greater

names = ["Alex", "Balde", "Bukkati", "Rexxie"]

# scores = [stu_score for stu_score in names]

scores = {student: random.randint(1,100) for student in names}
passed_students = {student: score for (student, score) in scores.items() if score > 60}
# print(scores)
# print(passed_students)

student_dict = {
    "name": ["Alex", "Balde"],
    "score": [20, 30]
}

std_df = pandas.DataFrame(student_dict)
for (index, row) in std_df.iterrows():
    print(index, row)
# print(std_df)