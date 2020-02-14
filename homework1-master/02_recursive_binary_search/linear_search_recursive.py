#!/usr/bin/env python
# encoding: utf-8

from hypothesis import given, settings
import hypothesis.strategies as st


def linear_search(search_list, item, pos=0):
    """Search search_list from left to right for item.

    This is a recursive function implementation of the algorithm.

    Parameters
    ----------
    search_list : list
        list to be searched
    item : any
        item we are looking for
    pos : int
        start position for search; defaults to 0
        
    Returns
    -------
    int or False

    Examples
    --------
    >>> linear_search([0,1,7,9], 7)
    2

    >>> linear_search([0,1,7,9], 8)
    False
    """
    # Base Case 1: list is empty
    if not search_list: 
        return False
    # Base Case 2: item found
    elif search_list[0] == item:
        return pos
    # Iteration Case:
    # - remove first element from list
    # - run binary search on remainder
    # - don't forget to increment pos
    else:
        return linear_search(search_list[1:], item, pos+1)


@given(search_list=st.lists(st.integers()),
       item=st.integers())
@settings(max_examples=1000)
def test_linear_search(search_list, item):
    if item in search_list:
        pos = linear_search(search_list, item)
        assert search_list[pos] == item
    else:
        assert linear_search(search_list, item) is False
