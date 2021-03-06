# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:53:25 2020

@author: Subiksha Godfrey
"""

# =============================================================================
# Problem Statement​ ​1:
# Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.
# =============================================================================

subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping over each of the predicates
sentence_list = [(subj+" "+ vrb + " " + objt) for subj in subject for vrb in verb for objt in obj]
for sentence in sentence_list:
 print (sentence)