#!/usr/bin/env python

# set is a collection of distinct elements
# a subset "s" is a set whose elements all come from set "S"
# the empty is the set with no elements 
# the powerset of "S" is the set of all subsets of "S"
# a family is a set of sets
# a member is a set within a family
# a family is union-closed as long as there is no way to union its members to create a new set that is not already one of the members of the family.
# any finite union closed family (except {}) has at least one element appearing in at least half the members 

# imports type signatures 
import typing
import numpy as np

# tests to see if a family is union closed
def is_union_closed(family: typing.Set[typing.Set[int]]) -> bool:
    for member in family:
        for other_member in family:
            if member != other_member:
                if not member.union(other_member) in family:
                    return False
    return True

# tests to see if a family conforms to the conjecture
def meets_conjecture(family: typing.Set[typing.Set[int]]) -> bool:
    if not is_union_closed(family):
        return False
    count = 0
    for member in family:
        for other_member in family:
            if member != other_member:
                if member.issubset(other_member) or other_member.issubset(member):
                    count += 1
        if count < len(family)/2:
            return False
    return True

def normalize_family(family: typing.Set[typing.Set[int]]) -> [[int]]:

    # gets the size of the family
    family_size = len(family)

    normalized_family = []

    # extracts the distinct elements from the members of the family
    distinct_elements = set()
    for member in family:
        distinct_elements = distinct_elements.union(member) 
    distinct_elements = list(distinct_elements)
    distinct_elements.sort()


    # creates a matrix of zeros with the number of rows equal to the number of members in the family and the number of columns equal to the number of distinct elements
    normalized_family = np.zeros((family_size, len(distinct_elements)), dtype=int)
    for member in family:
        for element in member:
            normalized_family[family.index(member)][distinct_elements.index(element)] = 1
    return normalized_family
    """
    bitstring_size = len(bin(len(distinct_elments) - 1)[2:])
    for i in range(1, family_size + 1):
        bitstring = [*(bin(i)[2:])]
        leading_zeros = bitstring_size - len(bitstring)
        bitstring = [0]*leading_zeros + [int(x) for x in bitstring]
        family.append(bitstring)
    return np.array(family)
    """

def normalize_meets_conjecture(family_size: int) -> bool:
    normalized_family = normalize_family(family_size)
    cx = normalized_family.sum(axis=0)/(len(normalized_family) - 1)
    print(cx)
    if np.all(cx < 0.5):
        return False
    return True

# tests to see if normalize_family works as expected
"""
for i in range(1,5):
    print(i,normalize_meets_conjecture(i))
"""

#print(normalize_meets_conjecture(5000000))

# examples of the is_union_closed and meets_conjecture functions

# uses the existing functions to prove the conjecture



"""
#print(normalize_family(4))
def prove_conjecture(family_size: int) -> bool:
    family = normalize_family(family_size)
    return meets_conjecture(family)
set_family1 = [{1,2,3}, {2,3,4}, {3,4,5}, {4,5,6}]
print(is_union_closed(set_family1))
print(meets_conjecture(set_family1))
set_family2 = [{1,2}, {2}, {1}]
print(is_union_closed(set_family2))
print(meets_conjecture(set_family2))
"""

























set_family3 = [{1,2,3}, {2,3}, {1}]

"""
000 = {}
001 = {1}
010 = {2}
100 = {3}
011 = {1,2}
110 = {2,3}
101 = {1,3}
111 = {1,2,3}


0000000 = {}
0000001 = {1}
0000011 = {1,2}
0000111 = {1,2,3}
0001111 = {1,2,3,4}
0011111 = {1,2,3,4,5}
0111111 = {1,2,3,4,35,26}
1111111 = {1,2,3,4,35,26,57}
"""
set_family4 = [{1,2,3,4,5,6,7}, {1,2,3,4,5,6}, {1,2,3,4,5}, {1,2,3,4}, {1,2,3}, {1,2}, {1}]
print(normalize_family(set_family4))
