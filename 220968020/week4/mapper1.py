import sys
for line in sys.stdin:
    line = line.strip()   
    fields = line.split(',')
    if len(fields) == 3 and fields[0].startswith("STU"):
        student_id, name, course_id = fields
        print(f"{course_id}\tS\t{student_id},{name}")
    elif len(fields) == 3 and not fields[0].startswith("STU"):
        course_id, course_name, sem = fields
        print(f"{course_id}\tC\t{course_name},{sem}")

