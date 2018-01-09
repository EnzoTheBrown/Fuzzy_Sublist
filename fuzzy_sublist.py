from Levenshtein import ratio
from operator import and_, or_
from functools import reduce
from graph import *
from graphviz import Digraph


def display(l, sublist, threshold, result, candidates):
    print("Possibles sentences that we can understand from "+ str(sublist) + " with a threshold of " + str(threshold))
    print('the layers of the graph are:')
    print(list(map(lambda x: x[1], candidates)))
    print('Is there a fuzzy-sublist of '  + str(l) + ' in those? ' + str(result))

def build_graph_layer(words, nodes, list_nodes, list_cand):
    new_nodes = [Node(word) for word in words]
    list_cand.append(new_nodes)
    for node in new_nodes:
        list_nodes.append(node)
    for node in nodes:
        for new_node in new_nodes:
            node.add_neighb(new_node)
    return new_nodes

def build_whole_graph(candidates, nodes, list_cand):
    first_nodes = build_graph_layer(candidates[0][1], [], nodes, list_cand)
    current_nodes = first_nodes
    for _, candidate in candidates[1:]:
        current_nodes = build_graph_layer(candidate, current_nodes, nodes, list_cand)
    return first_nodes

def is_sublist_fuzzy(l, sublist, threshold, visu=False, name="test.gv"):
    print('#'*50)
    if sublist == []:
        print('The empty list is a fuzzy-sublist of any list')
        return True
    # if the list is empty and not the sublist then return False
    if l == []:
        print('The empty list as no fuzzy-sublist appart from itself')
        return False
    candidates = [(i_sublist, l) for i_sublist in sublist]
    candidates = [(candidate, list(set(filter(lambda word: ratio(candidate, word) > threshold, words)))) for candidate, words in candidates]
    nodes = []
    list_cand = []
    first_nodes = build_whole_graph(candidates, nodes, list_cand)
    graph = Graph(first_nodes, nodes)
    result = graph.is_fuzzy_sublist(l)
    display(l, sublist, threshold, result, candidates)
    # rendering the graph
    if visu:
        dot = Digraph()
        graph.init_graphviz(dot)
        dot.render("test-output/"+name, view=False)
    return result






