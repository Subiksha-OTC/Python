# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:28:33 2020

@author: Subiksha Godfrey
"""

 #Reduce will produce a single result
def myreduce(Tryfunc, sequence):

 # Get first item in sequence and assign to result
  sum = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   sum = Tryfunc(sum, item)

  return sum

print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [35,45,3])) )

# list of alphabets
Tryletters = ['a', 'b', 'd', 'e', 'p', 'j', 'i','s', 'o', 'r', 'u']

# function that filters non-vowels
def filter_non_vowel(Tryletters):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(Tryletters in vowels):
        return False
    else:
        return True 

filter_non_vowel = filter(filter_non_vowel, Tryletters)

print('The filtered non-vowels are:')
for non_vowel in filter_non_vowel:
    print(non_vowel)