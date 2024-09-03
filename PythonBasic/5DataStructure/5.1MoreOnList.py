#list.append(x) Add an item to the end of the list
#list.extend(iterable) Extend the list by appending all the items from the iterable.
#list.insert(i, x) : Insert an item at a given position. The first argument is the index of the element before which to insert
#list.remove(x) : Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item
#list.pop([i]) : Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
#list.clear() : Remove all items from the list. Equivalent to del a[:].
#list.index(x[, start[, end]]) : eturn zero-based index in the list of the first item whose value is equal to x.
#list.count(x) Return the number of times x appears in the list.
# list.sort(*, key=None, reverse=False) 
#list.reverse() reverse element in lisst
# list.copy() Return a shallow copy of the list

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)  # Find next banana starting at position 4
6
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'