"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
    def delete_from_list(list_to_clean, item_to_delete):
    if item_to_delete in list_to_clean:
        print('Initial list:', list_to_clean)
        print('Item to delete:', item_to_delete)
        findindex = list_to_clean.index(item_to_delete)
        list_to_clean.pop(findindex)
        print("List after deletion:",list_to_clean)
    else: 
        print('Item does not exist in the initial list:', list_to_clean)
        
delete_from_list(['A', 'B', 'C'], 'D')
delete_from_list([1, 2, 3, 4, 3], 3)
delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
delete_from_list([1, 2, 3], 'b')
delete_from_list([], 'b')
