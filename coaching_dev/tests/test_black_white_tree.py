import pytest
from collections import defaultdict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from coaching_dev.black_white_tree import BlackAndWhiteTreeSolver

@pytest.fixture
def sample_data():
    return {
        "case_1": {
            "n": 8,
            "edges": [(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (2, 6), (3, 7), (4, 8)],
            "expected": (0, 0, [])
        },
        "case_2": {
            "n": 8,
            "edges": [(1, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],
            "expected": (4, 1, [(1, 3)])
        },
        "case_3": {
            "n": 5,
            "edges": [(1, 2), (2, 3), (3, 4), (4, 1)],
            "expected": (1, 1, [(1, 5)])
        }
    }

def test_minimal_difference_coloring(sample_data):
    for case_name, case_data in sample_data.items():
        solver = BlackAndWhiteTreeSolver(case_data["n"], case_data["edges"])
        diff, added_count, added_edges = solver.minimal_difference_coloring()
        expected_diff, expected_count, expected_edges = case_data["expected"]
        assert diff == expected_diff, f"{case_name}: Expected diff {expected_diff}, got {diff}"
        assert added_count == expected_count, f"{case_name}: Expected added_count {expected_count}, got {added_count}"
        assert sorted(added_edges) == sorted(expected_edges), f"{case_name}: Expected edges {expected_edges}, got {added_edges}"

def test_tree_generator():
    generated_tree = BlackAndWhiteTreeSolver.tree_generator(10)
    assert len(generated_tree) == 9, "Generated tree should have n-1 edges."
    assert all(1 <= u <= 10 and 1 <= v <= 10 for u, v in generated_tree), "Nodes in the generated tree should be within range."

def test_bipartite_check():
    graph = defaultdict(list)
    edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    solver = BlackAndWhiteTreeSolver(4, edges)
    component = [1, 2, 3, 4]
    group1, group2 = solver.bipartite_check(component)
    assert set(group1 + group2) == set(component), "All nodes should be assigned to a group."
    assert all(u in group1 and v in group2 or u in group2 and v in group1 for u, v in edges), "Adjacent nodes should be in different groups."

def test_find_components():
    edges = [(1, 2), (3, 4), (5, 6)]
    solver = BlackAndWhiteTreeSolver(6, edges)
    components = solver.find_components()
    assert len(components) == 3, "Should find 3 components."
    assert sorted(map(sorted, components)) == [[1, 2], [3, 4], [5, 6]], "Components should match expected structure."
