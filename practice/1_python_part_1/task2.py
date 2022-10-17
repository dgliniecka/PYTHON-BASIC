"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict

def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    print("Dictionary before: ", dict_to_update)
    print("Items to set: ", items_to_set)
    if dict_to_update == {} and items_to_set != {}:
      dict_to_update = items_to_set
      print("Updated dictionary: ", dict_to_update)
      
      return dict_to_update
    elif dict_to_update != {} and items_to_set == {}:
      print("Updated dictionary: ", dict_to_update)
      return dict_to_update
    elif dict_to_update == {} and items_to_set == {}:
      print('Both values empty!')
      return dict_to_update
    else:
      for i in items_to_set.keys():
        if dict_to_update[i]<items_to_set[i]:
          dict_to_update[i]=items_to_set[i]
          print("Updated dictionary: ", dict_to_update)
          return dict_to_update
       
set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
set_to_dict({}, a=0)
set_to_dict({'a': 5})
