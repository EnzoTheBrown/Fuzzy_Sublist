from Levenshtein import ratio
from functools import reduce
from operator import or_


def get_all_sublists(list_, n):
    result = []
    for i in range(len(list_) - n + 1):
        result.append(list_[i:i+n])
    return result

def is_list_fuzzy(l, ll, threshold):
    print('-'*50)
    for i_l in range(len(l)):
       print(l[i_l], ll[i_l], ratio(l[i_l], ll[i_l]))
       if ratio(l[i_l], ll[i_l]) < threshold:
           return False
    return True

def is_sublist_fuzzy(l, sublist, threshold):
    print('#'*50)
    if len(sublist) > len(l):
        return False
    if sublist == []:
        return True
    sublists = get_all_sublists(l, len(sublist))
    return reduce(or_, [is_list_fuzzy(sublist, i, threshold) for i in sublists], False)

