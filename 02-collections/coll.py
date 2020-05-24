#! /usr/bin/env python3
# encoding: UTF-8
#
# Python Workshop - Collections
#

import random

#
# Shared variables
#
N = 11
xs = list(range(1, N+1)) * 2  # The numbers 1 to N repeated twice
random.shuffle(xs)  # shuffle the list
print(f'xs = {xs}')


#
# findMin
#
def findMin(xs):
    '''findMin returns the SMALLEST number in the list xs'''
    # FIXME Implement me
    return -1


# Test
print(f'Smallest value found: {findMin(xs)} (expected 1)')


#
# findSum
#
def findSum(xs):
    '''findSum returns the SUM of the numbers in xs'''
    # FIXME Implement me
    return 0


# Test
exp = 2 * N*(N+1)//2
print(f'Sum of values: {findSum(xs)} (expected {exp})')


#
# sortList
#
def sortList(xs):
    '''Return a sorted copy of xs'''
    # FIXME Implement me
    return xs

# Test
# Can you write your own test case?


#
# removeDuplicates
#
def removeDuplicates(xs):
    '''removeDuplicates removes duplicate items from the list xs.
    Items should be kept in the same order.

    removeDuplicates([3, 2, 4, 2, 6, 4]) => [3, 2, 4, 6]
    '''
    # FIXME Implement me
    return xs


# Test
# Can you write your own test case?
