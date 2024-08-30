def expectations():
    items = {
        "case_1": {"intervals": [[1, 2], [2, 3], [3, 4], [1, 3]], "expected": 1},
        "case_2": {"intervals": [[1, 2], [1, 2], [1, 2]], "expected": 2},
        "case_3": {"intervals": [[1, 2], [2, 3]], "expected": 0},
    }
    return items
