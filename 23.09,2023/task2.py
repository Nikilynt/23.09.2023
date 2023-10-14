#Mykyta
#Task 2
#23.09.2023


N = int(input('Enter: '))
a = [int(s) for s in input().split()]
p = int(input('Enter: '))
a.insert(0,a.pop(p-1))
print(' '.join([str(i) for i in a]))