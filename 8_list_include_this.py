import sys

def include(arr, item):
  return True if item in arr else False

my_list = sys.argv[1]
iten = sys.argv[2]
print(include(my_list, iten))

