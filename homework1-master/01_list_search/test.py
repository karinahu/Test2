#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# load our search functions from the other files
from linear_search import linear_search
from binary_search import binary_search

# load our timing module
import timeit

# load random module for creating a random list
import random


'''def random_list(list_length=1):
    return [random.randint(0, 100000)
            for _ in range(list_length)]'''

def random_sorted_list(list_length=1):
    random_sorted_list=sorted(random.randint(0, 100000))
            for _ in range(list_length)]
    return random_sorted_list


def time_search_algorithms(list_length=1,
                           generator=random_sorted_list):
    # generate a sample list and search_item
    search_list = generator(list_length=list_length)
    search_item = random.randint(0, 10000)

    # dictionary for storing values
    times = {}
    # keep track of list length
    times['length'] = list_length

    start_time = timeit.default_timer()
    linear_search(search_list, search_item)
    duration = timeit.default_timer() - start_time
    times['linear'] = duration

    start_time = timeit.default_timer()
    binary_search(sorted(search_list), search_item)
    duration = timeit.default_timer() - start_time
    times['binary'] = duration

    return times


def run_tests(generator=random_list):
    for length in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        print("Testing list of length {}".format(str(length)))
        times = time_search_algorithms(list_length=length,
                                       generator=generator)
        print("Linear search: {}".format(str(times['linear'])))
        print("Binary search: {}".format(str(times['binary'])))
        print()
