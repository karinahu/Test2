#!/usr/bin/env python
# encoding: utf-8

#from hypothesis import given, settings
#import hypothesis.strategies as st


def binary_search(search_list, item,pos=0):
   
    """Search search_list from left to right for item.

    This is a recursive function implementation of the algorithm.

    Parameters
    ----------
    search_list : list
        list to be sorted, but all elements in the list must be the same type
    item : number or alphabet
        item must be the same type as in the list
    pos : int
        start position for search; defaults to 0
        
    Returns
    -------
    True or False

    Examples
    --------
    >>> binary_search(['a','c','e','h','s'],'e',pos=0)
    True
    >>> binary_search(['a','c','e','h','s'],'d',pos=0)
    False
    """
    search_list=sorted(search_list)
    
    if len(search_list)==0:
        return False

    mid=len(search_list)//2

    if search_list[mid]==item:
        return True
    
    elif search_list[mid]>item:
        return binary_search(search_list[:mid],item,pos=0)

    else:
        return binary_search(search_list[mid+1:],item,pos=0)

    return False
    

 
            

'''# code for unit testing
# first we define our variables:
# - search_list is a random list of integers
# - item is a random integer
@given(search_list=st.lists(st.integers()),
       item=st.integers())
# now we ask Python to generate 1000 such examples
@settings(max_examples=1000)
# and this is our testing function:
def test_binary_search(search_list, item):
    # if search_list contains item,
    # verify that binary_search returns the position
    # where the item is in search_list
    if item in search_list:
        pos = binary_search(search_list, item)
        assert search_list[pos] == item
    # if item is not in search_list,
    # binary_search should return False
    else:
        assert binary_search(search_list, item) is False'''
