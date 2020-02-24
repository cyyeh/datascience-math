# tuples
from itertools import product

print("tuples")
for c in product("abc", repeat=2):
  print("".join(c))

# permutations
from itertools import permutations

print("permutations")
for c in permutations("abc", 2):
  print("".join(c))

# combinations
from itertools import combinations

print("combinations")
for c in combinations("abc", 2):
  print("".join(c))

# combinations with repetitions
from itertools import combinations_with_replacement

print("combinations with repetitions")
for c in combinations_with_replacement("abc", 2):
  print("".join(c))
