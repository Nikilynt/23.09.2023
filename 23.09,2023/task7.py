#Mykyta
#Task 4
#23.09.2023

N = int(input('Enter: '))
pupils = {}
Marks_count = 3

for _ in range (N):
    pupil = input('Enter: ').split()
    pupils[pupil[0]] = [int(i) for i in pupil[1 :]]
    print('%s %.2f' % (pupil[0],
        sum(pupils[pupil[0]]) / Marks_count))
