#!/usr/bin/env python
# encoding: utf-8



def selection_sort(unsorted_list):
    '''List will be sorted by selection sort algorithm

    This algorithm is more efficient than linear sort

    Parameters
    ----------
    unsorted_list: list

    Return
    ------
    list
    list to be sorted

    Examples
    --------
    >>> unsorted_list=[1,7,4,5,2]
    >>> selection_sort(unsorted_list)
    [1, 2, 4, 5, 7]
    
    '''

    
    for i in range(0,len(unsorted_list)-1):
        min_index=i
        for j in range(i+1,len(unsorted_list)):
            if unsorted_list[min_index]>unsorted_list[j]:
                min_index=j

        unsorted_list[i],unsorted_list[min_index]=unsorted_list[min_index],unsorted_list[i]
    return unsorted_list


