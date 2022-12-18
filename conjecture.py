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

def normalize_family(family_size: int) -> [[int]]:
    family = []
    bitstring_size = len(bin(family_size - 1)[2:])
    for i in range(0, family_size):
        bitstring = [*(bin(i)[2:])]
        leading_zeros = bitstring_size - len(bitstring)
        bitstring = [0]*leading_zeros + [int(x) for x in bitstring]
        family.append(bitstring)
    return np.array(family)


# tests to see if normalize_family works as expected
print(normalize_family(17))

# examples of the is_union_closed and meets_conjecture functions
"""
set_family1 = [{1,2,3}, {2,3,4}, {3,4,5}, {4,5,6}]
print(is_union_closed(set_family1))
print(meets_conjecture(set_family1))
set_family2 = [{1,2}, {2}, {1}]
print(is_union_closed(set_family2))
print(meets_conjecture(set_family2))
set_family3 = [{1,2,3}, {2,3}, {1}]
print(is_union_closed(set_family3))
print(meets_conjecture(set_family3))
"""
