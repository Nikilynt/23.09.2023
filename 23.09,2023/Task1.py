#Mykyta
#Task 1
#23.09.2023

N = int(input('Enter: '))
a = [int(s) for s in input().split()]
p = int(input('Enter: '))
print(' '.join([str(i) for i in a if i != p]))