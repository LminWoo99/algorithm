from itertools import combinations
from itertools import permutations
data=[1,2,3,4,5,6]
it=combinations(data,3)
pd=permutations(data,2)
print(*it)
print(*pd)