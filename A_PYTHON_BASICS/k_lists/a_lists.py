# List
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Create a List
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Lists allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Print the number of items in the list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]
print(list1) 

# What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # Output: <class 'list'>

# Using the list() constructor to make a List
thislist = list(("apple", "banana", "cherry"))
print(thislist)