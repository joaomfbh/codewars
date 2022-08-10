#k kata link
# https://www.codewars.com/kata/545991b4cbae2a5fda000158

'''
Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.
'''

def include(arr, item):
  return True if item in arr else False

my_list = sys.argv[1]
iten = sys.argv[2]
print(include(my_list, iten))

