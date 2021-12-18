#!/usr/bin/env python3
"""simple helper function"""


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters"""
    last_page = page * page_size
    start = last_page - page_size
    tup = (start, last_page)
    return tup
