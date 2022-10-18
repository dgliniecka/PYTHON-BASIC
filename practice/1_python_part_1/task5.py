"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""
def remove_duplicated_words(line: str) -> str:
  result = ""
  line = line.split()
  line = sorted(set(line))
  for l in line:
    result = result + l + " "
  print('Final string:', result)
  result = result[:-1]
  return result

remove_duplicated_words('cat cat dog 1 dog 2')
remove_duplicated_words('cat cat cat')
remove_duplicated_words('1 2 3')
