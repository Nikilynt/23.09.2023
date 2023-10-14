#Mykyta
#Task 3
#23.09.2023

N = int(input('Enter: '))
a = [int(s) for s in input().split()]
p = int(input('Enter: '))
del a[p - 1]
(Q, K) = [int(s) for s in input().split()]
a.insert(Q - 1, K)
print(' '.join([str(i) for i in a]))