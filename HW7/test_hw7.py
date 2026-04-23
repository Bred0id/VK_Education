import pytest
from first import has_cycle
from second import is_tree
from third import dijkstra
from fourth import is_bipartite

def test_first_cycle():
    g1 = {0: [1], 1: [0, 2], 2: [1]}
    assert has_cycle(g1) is False
    g2 = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert has_cycle(g2) is True
    g3 = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2], 4: [5], 5: [4, 6], 6: [5, 7], 7: [6]}
    assert has_cycle(g3) is False
    g3[5].append(7)
    g3[7].append(5)
    assert has_cycle(g3) is True

def test_second_is_tree():
    tree = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    assert is_tree(tree, 0) is True
    cycle_graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert is_tree(cycle_graph, 0) is False
    disconnected = {0: [1], 1: [0], 2: [3], 3: [2]}
    assert is_tree(disconnected, 0) is False
    assert is_tree({}, 0) is True

def test_third_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 5},
        'B': {'A': 1, 'C': 2, 'D': 3},
        'C': {'A': 5, 'B': 2, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }
    dist = dijkstra(graph, 'A')
    assert dist == {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    single = {'X': {}}
    assert dijkstra(single, 'X') == {'X': 0}

def test_fourth_bipartite():
    bipartite1 = {0: [1], 1: [0, 2], 2: [1]}
    assert is_bipartite(bipartite1) is True
    triangle = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert is_bipartite(triangle) is False
    bipartite2 = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2],
        4: [5],
        5: [4]
    }
    assert is_bipartite(bipartite2) is True
    assert is_bipartite({}) is True