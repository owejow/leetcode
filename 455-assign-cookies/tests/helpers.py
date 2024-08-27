def expectations():
    items = {
        "example_1": {"greed": [1, 2, 3], "size": [1, 1], "expected": 1},
        "example_2": {"greed": [1, 2], "size": [1, 2, 3], "expected": 2},
        "example_3": {"greed": [4, 5, 6], "size": [1, 2, 3], "expected": 0},
        "example_4": {"greed": [], "size": [1, 2, 3], "expected": 0},
        "example_5": {"greed": [1, 2, 3], "size": [], "expected": 0},
    }
    return items
