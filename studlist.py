import random

def student_in_dict(stud):
    stud_list = []
    for student_str in stud:
        student = student_str.split(';')
        stud_list.append({'id': int(student[0]), 'name': student[1], 'gender': student[2], 'number': int(student[3])})
    return stud_list


def bubble_sort(stud, key):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(stud) - 1):
            if stud[i][key] > stud[i + 1][key]:
                stud[i], stud[i + 1] = stud[i + 1], stud[i]
                swapped = True
    return stud

def reverse_bubble_sort(stud, key):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(stud) - 1):
            if stud[i][key] > stud[i + 1][key]:
                stud[i], stud[i + 1] = stud[i + 1], stud[i]
                swapped = True
    return stud[::-1]


stud = open('stud.txt', 'r', encoding="utf-8")
student_list = student_in_dict(stud)
stud.close()

random.shuffle(student_list)

print(bubble_sort(student_list, 'id'))
print(bubble_sort(student_list, 'number'))

print(reverse_bubble_sort(student_list, 'id'))