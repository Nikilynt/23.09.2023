# Mykyta
# Task 5
# 23.09.2023

N = int(input('Enter: '))
pupils = {}
Marks_count = 3

for _ in range(N):
    pupil = input().split()
    pupil[1:] = [int(i) for i in pupil[1:]]
    pupil.insert(0, -sum(pupil[1:]) / Marks_count)
    pupils.append(pupil)

pupils.sort()
for p in pupils:
    print('%s %s $.2f' %
          (p[1],
           ''.join([str(mark) for mark in p[2 : ]]),
           p[0]
           ))