import sys
from collections import defaultdict


course_data = {}

students_data = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    course_id, record_type, data = line.split('\t')

    if record_type == 'C': 
        course_data[course_id] = data 
    elif record_type == 'S': 
        student_id, student_name = data.split(',')
        students_data[course_id].append((student_id, student_name))  

for course_id in course_data:
    if course_id in students_data:
        for student in students_data[course_id]:
            print(f"{student[0]}, {student[1]}, {course_id}, {course_data[course_id]}")

