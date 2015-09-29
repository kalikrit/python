#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Weights Manager
    description: split given weights list by number of platforms
    programming language: Python (3.4.0)
    
author: Konstantin Kononenko (Moscow, Russia)
email: kali-krit@mail.ru
date: 29.09.2015
version: 1.1.7

"""

def gen_all_subsets(given_set):
    """
    function generates all possible subsets of the given set
    return set
    """
    subsets = [()]
    for item in given_set:
        for subset in subsets:
            subsets = subsets + [tuple(subset) + (item,)]
           
    return set(subsets)

def select_subset_for_platform(given_set, weights_per_platform):
    """
    finds all subsets which sums to weights_per_platform
    return list
    """
    subsets = gen_all_subsets(given_set)
    candidates = []
    for subset in subsets:
        if sum(subset) <= weights_per_platform:
            candidates.append(subset)
    max_result = 0
    selected_set = []
    for candidate in candidates:
        if sum(candidate) > max_result:
            max_result = sum(candidate)
            selected_set = candidate
    return selected_set
    
def exclude_set(from_set, given_set):
    """
    helper function that substracts set from set
    return list
    """
    from_set = list(from_set)
    given_set = list(given_set)
    result = []
    for item in from_set[:]:
        if item in given_set[:]:
            from_set.remove(item)
            given_set.remove(item)
        else:
            result.append(item)
    return result        
    
def main(weights_list = [], num_of_platforms = 2, match_sum = 100):
    """
    main function
    manage list of weights by number of platforms
    prints subsets for each platform
    by default num_of_platforms is 2
    
    also prints whether there are subsets sums to match_sum (by default 100)
    """
    # checking whether weights_list is not empty
    if len(weights_list) < 1:
        print('weights list should be set of natural numbers')
        return
    # checking whether weights_list length is greater than number of platforms
    if len(weights_list) < num_of_platforms:
        print('weights list should be greater than number of platforms')
        return
    # checking whether weights_list is not too long
    if len(weights_list) > 15:
        print("the programm is not optimized for such a long list")
        print("computation will take a long time")
        return
    
    print("managing ", weights_list, " by ", num_of_platforms, " platforms...")
    weights_per_platform = float(sum(weights_list)) / num_of_platforms
    print('weights per platform: ', weights_per_platform)
    print()
    
    weights_copy = weights_list[:]
    iter = 1
    while iter < num_of_platforms:
        temp = select_subset_for_platform(weights_copy, weights_per_platform)
        print(temp, sum(temp))
        weights_copy = exclude_set(weights_copy, temp)
        iter += 1
    print(tuple(weights_copy), sum(weights_copy))
    
    print()
    match = False
    all_subsets = gen_all_subsets(weights_list)
    for subset in all_subsets:
        if sum(subset) == match_sum:
            match = True
            print("this subset sums to ", match_sum, ' : ', subset)
            
    if not match: print('there are no subsets which sums to', match_sum)


if __name__ == "__main__":
    
    print()
    print("enter list of natural numbers separated by '<space>'")
    user_input = input()

    # check user input: just select all positive numbers
    weights_list = []
    for item in user_input.split(' '):
        try:
            num = int(item)
            if num > 0:
                weights_list.append(num)
        except Exception:
            pass
    print()
    
    #weights_list = (1,1,2,3,5)
    #weights_list = (1,3,2,3)
    
    #weights_list = (5,5,4,4,5,4)
    #main(weights_list, 3)
    
    #weights_list = (1,5,7,12)
    #weights_list = (10,20,2,80,30,15,3,15,18,8)
    #weights_list = (11,15,26,7,1,2,16,27,12,5,8,10,22,20,30)    
    #main(weights_list, 4, 200)
    
    main(weights_list)