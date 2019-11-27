#! /usr/bin/env python3
# encoding: UTF-8
#
# Python Workshop - Collections
#

import random


#
# findMin
#
def findMin(xs):
    '''findMin return the SMALLEST number in the list xs'''
    # FIXME Implement me
    return 0


# Test
N = random.randint(1, 1000)
xs = list(range(1, N+1))
random.shuffle(xs)  # shuffle the list
print(findMin(xs), '==?', 1)


#
# findSum
#
def findSum(xs):
    '''findSum returns the SUM of the numbers in xs'''
    # FIXME Implement me
    return 0


# Test
N = random.randint(1, 1000)
print(findSum(range(N+1)), '==?', N*(N+1)//2)


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
