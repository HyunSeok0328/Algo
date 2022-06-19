from itertools import permutations
from itertools import combinations

arr = [1,2,3,4,5]
for i in permutations(arr,2) :
    print(i, end = ' ')
print('')
for i in combinations(arr,2) :
    print(i, end = ' ')
