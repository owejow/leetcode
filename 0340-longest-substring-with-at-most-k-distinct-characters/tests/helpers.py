def expectations():
    items = {
        "case_1": {"s": "aabbcc", "k": 1, "expected": 2},
        "case_2": {"s": "aabbcc", "k": 2, "expected": 4},
        "case_3": {"s": "aabbcc", "k": 3, "expected": 6},
        "case_4": {"s": "aabbcc", "k": 3, "expected": 6},
        "case_5": {"s": "abbbbbc", "k": 1, "expected": 5},
        "case_6": {"s": "abbabaaaabbc", "k": 2, "expected": 11},
        "case_7": {"s": "abbabaaaabbc", "k": 0, "expected": 0},
        "case_8": {"s": "eceba", "k": 2, "expected": 3},
        "case_9": {"s": "araaci", "k": 2, "expected": 4},
        "case_9": {"s": "araaci", "k": 20, "expected": 6},
    }
    return items
