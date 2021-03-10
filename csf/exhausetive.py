from itertools import permutations

arr = list(range(2, 26))

all_c = permutations(arr, len(arr))

# i+=1

# for l in all_c:
#     print()

t = 1

for i in range(1, 26):
    t = t*i

print(t)