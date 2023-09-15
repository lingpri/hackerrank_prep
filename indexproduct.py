import math
import os
import random
import re
import sys


def split_array(n, index):
    left_array, right_array = [],[]
    left_array = n[0:index]
    right_array = n[index+1:len(n)]
    return left_array,right_array

def get_left_closest_max_value(array, element):
    for index, item in reversed(list(enumerate(array))):
        if (item > element):
            return index + 1
    return 0

def get_right_closest_max_value(array, element,offset):
    for index, item in enumerate(array):
        if (item > element):
            return index + offset + 2
    return 0

def get_left_and_right_stack(randarr):
    leftstack = []
    rightstack = []
    for i,item in enumerate(randarr):
        left_array, right_array = split_array(randarr,i)
        leftpos = get_left_closest_max_value(left_array, item)
        rightpos = get_right_closest_max_value(right_array,item,len(left_array))
        leftstack.append(leftpos)
        rightstack.append(rightpos)
    return leftstack,rightstack


def solve(arr):
    leftstack,rightstack = get_left_and_right_stack(arr)
    multiplied = [ left * right for left,right in zip(leftstack, rightstack)]
    return max(multiplied)

