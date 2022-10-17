"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List
def calculate_power_with_difference(ints: List[int], power: int) -> List[int]:
  new = ints.copy()
  new[0] = new[0] ** power
  length = len(ints)
  i = 1
  while i < length:
    new[i] = new[i] ** power
    new[i] = new[i] - (new[i-1] - ints[i-1])
    i += 1
  print(new)
  return new

calculate_power_with_difference([1, 2, 3], 2)
