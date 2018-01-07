# Enzo Lebrun
# enzo.the@gmail.com
from fuzzy_sublist import *


def runtests():
    # cheking is_sublist_fuzzy
    l = ['je', 'mange', 'une', 'pomme']
    sublist = ['manga', 'un', 'pimme']
    sublist2 = ['ye', 'pommge', 'un', 'pomange']
    sublist3 = ['je', 'un', 'pimme']
    sublist4 = ['ye', 'pommge', 'pomange']

    # checking sides effects
    assert is_sublist_fuzzy([], [], 0.7)
    assert not is_sublist_fuzzy([], l, 0.7)
    assert is_sublist_fuzzy(l, [], 0.7)

    assert is_sublist_fuzzy(l, sublist, 0.7)
    # checking if the order in the sublist is respected
    assert not is_sublist_fuzzy(l, sublist3, 0.7)
    # checking if l == l
    assert is_sublist_fuzzy(l, l, 0.99)

    # 'pommge' is more likely to be 'pomme' than 'mange',
    # so the most probable sentence is "je pomme une mange"
    # but the real fuzzy-sublist is "je mange une pomme"
    # so we need to verify if is_sublist_fuzzy handle those kind of sides effects
    assert is_sublist_fuzzy(l, sublist2, 0.4)
    # checking if the order in the list still matters
    assert not is_sublist_fuzzy(l, sublist4, 0.4)


    # cheking when the threshold is 0
    assert is_sublist_fuzzy(l, sublist2, 0)
    # we need to verify that len(l) >= len(sublist)
    assert not is_sublist_fuzzy(['aaa'], ['ddd', 'bbb', 'ccc'], 0)



if __name__ == "__main__":
    runtests()


