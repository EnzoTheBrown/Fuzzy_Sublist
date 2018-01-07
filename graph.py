from functools import reduce
from operator import or_


class Node:
    def __init__(self, word):
        self.word = word
        self.neighbs = []

    def add_neighb(self, node):
        self.neighbs.append(node)

    def is_fuzzy_sublist(self, words):
        # for each sublist of words
        # we are checking if one of them fits to the graph
        return reduce(or_, [self.walk_in_graph(words[i:]) for i in range(len(words))], False)

    def walk_in_graph(self, words):
        # if there is no more words and the graph continues:
        if len(words) == 0:
            return False
        # if the word is different to the node
        if words[0] != self.word:
            return False
        # if the graph ended
        if len(self.neighbs) == 0:
            return True
        # otherwise we check for every possible path if one of them fits to the remaining words
        return reduce(or_, [neighb.walk_in_graph(words[1:]) for neighb in self.neighbs], False)


class Graph:
    def __init__(self, first_nodes):
        self.first_nodes = first_nodes

    def is_fuzzy_sublist(self, l):
        return reduce(or_, [node.is_fuzzy_sublist(l) for node in self.first_nodes], False)


def run_graph_tests():
    mange = Node('mange')
    une = Node('une')
    pomme = Node('pomme')
    pomme2 = Node('pomme')
    mange2 = Node('mange')

    pomme2.add_neighb(une)
    mange.add_neighb(une)
    une.add_neighb(pomme)
    une.add_neighb(mange2)

    test = ['je', 'mange', 'une', 'pomme']
    assert mange.is_fuzzy_sublist(test)
    assert une.is_fuzzy_sublist(test)


run_graph_tests()


