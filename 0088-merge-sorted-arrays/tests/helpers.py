def expectations():
    items = {
        "case_1": {
            "nums1": [1, 2, 3, 0, 0, 0],
            "m": 3,
            "nums2": [2, 5, 6],
            "n": 3,
            "expected": [1, 2, 2, 3, 5, 6],
        },
        "case_2": {
            "nums1": [1],
            "m": 1,
            "nums2": [],
            "n": 0,
            "expected": [1],
        },
        "case_3": {
            "nums1": [0],
            "m": 0,
            "nums2": [1],
            "n": 1,
            "expected": [1],
        },
        "case_4": {
            "nums1": [2, 0],
            "m": 1,
            "nums2": [1],
            "n": 1,
            "expected": [1, 2],
        },
    }
    return items
