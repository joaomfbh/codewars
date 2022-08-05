# kata link
# https://www.codewars.com/users/joaomfbh/completed_solutions

'''
Complete the solution so that it reverses all of the words within the string passed in.

Example(Input --> Output):

"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
'''

def reverse_words(s):
    list_s = s.split()
    list_s.reverse()
    return ' '.join(list_s)
  
  
