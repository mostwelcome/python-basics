piano_keys = ['a', 'b', 'c', 'd', 'e', 'f']

piano_tuple = ('aa', 'bb', 'cc', 'dd', 'ee')

'''slicing works with both list and tuple in the same way'''

print(piano_keys[2:5])

print(piano_keys[:3])

# last is the interval
print(piano_keys[::2])

# reverse the list
print(piano_keys[::-1])

# reverse the tuple
print(piano_tuple[::-1])
