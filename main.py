# Enzo Lebrun
# enzo.the@gmail.com
from sublist import *


def runtests():
    # cheking is_sublist_fuzzy
    l = ['je', 'mange', 'une', 'pomme']
    sublist = ['manga', 'un', 'pimme']
    sublist2 = ['ye', 'pommge', 'un', 'pomange']
    sublist3 = ['je', 'un', 'pimme']

    # checking sides effects
    assert is_sublist_fuzzy([], [], 0.7)
    assert not is_sublist_fuzzy([], l, 0.7)
    assert is_sublist_fuzzy(l, [], 0.7)

    assert is_sublist_fuzzy(l, sublist, 0.7)
    # checking if the order in the sublist is respected
    assert not is_sublist_fuzzy(l, sublist3, 0.7)
    # checking if l == l
    assert is_sublist_fuzzy(l, l, 0.99)

    # cheking when the threshold is 0
    assert is_sublist_fuzzy(l, sublist2, 0)
    # we need to verify that len(l) >= len(sublist)
    assert not is_sublist_fuzzy(['aaa'], ['ddd', 'bbb', 'ccc'], 0)

    # advanced test:
    # the number of possibilities is exponential
    # so we need take care of the complexity of the algorithm
    l = "three switched witch watch three swatch watch switches which switched witch watches which swatch watch switch".split()
    sublist = "watches which swatch watch".split()
    assert is_sublist_fuzzy(l, sublist, 0.8)
    assert is_sublist_fuzzy(l, l, 0.5)

if __name__ == "__main__":
    runtests()


