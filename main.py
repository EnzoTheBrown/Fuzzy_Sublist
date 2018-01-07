# Enzo Lebrun
# enzo.the@gmail.com
from Levenshtein import ratio
from operator import and_, or_
from functools import reduce


def n_slices(n, list_):
    for i in range(len(list_) + 1 - n):
        yield list_[i:i+n]

def is_sublist(list_, sub_list):
    for slice_ in n_slices(len(sub_list), list_):
        if slice_ == sub_list:
            return True
    return False

def build_possible_sentences(i, list_, sentences, candidate):
    """
        use all the possible words for each position in order to build all the possible sentences
        for example the list (list_) [['a', 'b', 'c'],['g', 'h'],['e', 'f']]
        each list represent all the possible words that can be place at a given possition
        it will build the sentences (sentences):
        ['age', 'agf', 'ahe', 'ahf','bge', 'bgf', 'bhe', 'bhf','cge', 'cgf', 'che', 'chf']
    """
    if i == len(list_):
        sentences.append(candidate)
    else:
        for elem in list_[i][1]:
            build_possible_sentences(i+1, list_, sentences, candidate + [elem])

def is_candidate(list_):
    for i in list_:
        if i[1] == []:
            return False
    return True

def display(l, sublist, threshold, sentences, result):
    print("Possibles sentences that we can understand from "+ str(sublist) + " with a threshold of " + str(threshold))
    print(sentences)
    print('Is there a fuzzy-sublist of '  + str(l) + ' in those? ' + str(result))

def is_sublist_fuzzy(l, sublist, threshold):
    """
        is_sublist_fuzzy build every possible sentence we can understand from an input (sublist) and a list a words (l)
        with a given threshold (threshold), then it verifies if one of those possible sentence is a direct sublist of l
    """
    print('#'*50)
    print('the main sentence is ' + str(l))
    print('the fuzzy-sublist candidate is ' + str(sublist))
    print('the threshold is ' + str(threshold))
    # if the threshold equal 0 then we just need to verify the length of l and sublist
    if threshold == 0 and len(sublist) <= len(l):
        print('threshold = 0, there is no constraints')
        return True
    # handling sides effects here:
    # if sublist is empty then return True
    if sublist == []:
        print('The empty list is a fuzzy-sublist of any list')
        return True
    # if the list is empty and not the sublist then return False
    if l == []:
        print('The empty list as no fuzzy-sublist appart from itself')
        return False
    candidates = [(i_sublist, l) for i_sublist in sublist]
    # remove for each candidate the words with a ratio < threshold
    candidates = [(candidate, list(filter(lambda word: ratio(candidate, word) > threshold, words))) for candidate, words in candidates]
    # checking if there is no empty lists
    # otherwise it means some words of the candidate sublist does not have any fuzzy matching in l
    if not is_candidate(candidates):
        print('some word does not have any fuzzy-parents')
        return False
    # building every combinations of candidate words
    sentences = []
    build_possible_sentences(0, candidates, sentences, [])
    # display the result
    result = reduce(or_, [is_sublist(l, sentence) for sentence in sentences], False)
    display(l, sublist, threshold, sentences, result)
    # checking if at least one candidate sentence is a sublist of l
    return result


def runtests():
    # testing first functions
    # checking is_sublist function
    assert is_sublist(list(range(100)), [1,2,3,4,5])
    assert not is_sublist(list(range(100)), [1,2,7,8])
    assert is_sublist(list(range(100)), [])
    assert is_sublist([], [])
    assert not is_sublist([], list(range(100)))

    # checking build_possible_sentences
    candidates = [
            ['a', 'abc'],
            ['b', 'gh'],
            ['c', 'ef']
            ]
    sentences = []
    result = ['age', 'agf', 'ahe', 'ahf','bge', 'bgf', 'bhe', 'bhf','cge', 'cgf', 'che', 'chf']
    build_possible_sentences(0, candidates, sentences, [])
    # checking if build_possible_sentences return the elements in result
    assert set(map(lambda a: ''.join(a), sentences)) == set(result)

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


