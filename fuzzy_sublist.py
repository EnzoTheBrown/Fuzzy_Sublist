from Levenshtein import ratio
from operator import and_, or_
from functools import reduce
from graph import *


def display(l, sublist, threshold, result):
    print("Possibles sentences that we can understand from "+ str(sublist) + " with a threshold of " + str(threshold))
    print('Is there a fuzzy-sublist of '  + str(l) + ' in those? ' + str(result))

def build_graph_layer(words, nodes):
    new_nodes = [Node(word) for word in words]
    for node in nodes:
        for new_node in new_nodes:
            node.add_neighb(new_node)
    return new_nodes

def build_whole_graph(candidates):
    first_nodes = build_graph_layer(candidates[0][1], [])
    current_nodes = first_nodes
    for _, candidate in candidates[1:]:
        current_nodes = build_graph_layer(candidate, current_nodes)
    return first_nodes

def is_sublist_fuzzy(l, sublist, threshold):
    print('#'*50)
    if sublist == []:
        print('The empty list is a fuzzy-sublist of any list')
        return True
    # if the list is empty and not the sublist then return False
    if l == []:
        print('The empty list as no fuzzy-sublist appart from itself')
        return False
    candidates = [(i_sublist, l) for i_sublist in sublist]
    candidates = [(candidate, list(filter(lambda word: ratio(candidate, word) > threshold, words))) for candidate, words in candidates]
    first_nodes = build_whole_graph(candidates)
    result = Graph(first_nodes).is_fuzzy_sublist(l)
    display(l, sublist, threshold, result)
    return result
































