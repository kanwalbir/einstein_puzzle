#-----------------------------------------------------------------------------#
""" 
If the house numbers differ by 1, then the two persons live next to each other 
(neighbors).

Args: (i)  House number of person a
      (ii) House number of person b

Returns: (i) True or False
"""
def is_next(a, b):
    return abs(a - b) == 1

#-----------------------------------------------------------------------------#
""" 
If the house number of b is greater than the house number of a by 1, then 
a's house is left of b's house.

Args: (i)  House number of person a
      (ii) House number of person b

Returns: (i) True or False
"""
def is_left(a, b):
    return (b - a) == 1

#-----------------------------------------------------------------------------#
""" 
If the house number of a is greater than the house number of b by 1, then 
a's house is right of b's house.

Args: (i)  House number of person a
      (ii) House number of person b

Returns: (i) True or False
"""
def is_right(a, b):
    return (a - b) == 1

#-----------------------------------------------------------------------------#
