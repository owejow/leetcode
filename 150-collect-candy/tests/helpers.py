def expectations():
    items = {
        # checking single middle element
        "nil-empty-nil": {"candies": [], "count": 0, "sequence": None},
        "nil-single-nil": {"candies": [1], "count": 1, "sequence": [(0, 0, 0, 1)]},
        "nil-equal-nil": {"candies": [1, 1], "count": 2, "sequence": [(0, 0, 0, 2)]},
        "nil-decreasing-nil": {
            "candies": [3, 2, 1],
            "count": 6,
        },
        "nil-increasing-nil": {
            "candies": [1, 2, 3],
            "count": 6,
        },
        # nil decreasing
        "nil-decreasing-equal-two": {
            "candies": [3, 2, 1, 1],
            "count": 7,
        },
        "nil-decreasing-equal-three": {
            "candies": [3, 2, 1, 1, 1],
            "count": 8,
        },
        "nil-decreasing-increasing-one": {
            "candies": [3, 2, 1, 2],
            "count": 8,
        },
        "nil-decreasing-increasing-two": {
            "candies": [3, 2, 1, 2, 3],
            "count": 11,
        },
        "nil-decreasing-increasing-three": {
            "candies": [3, 2, 1, 2, 3, 4],
            "count": 15,
        },
        # nil equal
        "nil-equal-decreasing-one": {
            "candies": [2, 2, 1],
            "count": 4,
        },
        "nil-equal-decreasing-two": {
            "candies": [4, 4, 3, 2],
            "count": 7,
        },
        "nil-equal-decreasing-three": {
            "candies": [4, 4, 3, 2, 1],
            "count": 11,
        },
        "nil-equal-increasing-one": {
            "candies": [1, 1, 3],
            "count": 4,
        },
        "nil-equal-increasing-two": {
            "candies": [1, 1, 3, 4],
            "count": 7,
        },
        "nil-equal-increasing-three": {
            "candies": [1, 1, 3, 4, 5],
            "count": 11,
        },
        # nil increasing
        "nil-increasing-decreasing-one": {
            "candies": [1, 2, 3, 2],
            "count": 7,
        },
        "nil-increasing-decreasing-two": {
            "candies": [1, 2, 3, 2, 1],
            "count": 9,
        },
        "nil-increasing-decreasing-three": {
            "candies": [1, 2, 3, 2, 1, 0],
            "count": 13,
        },
        "nil-increasing-equal-one": {
            "candies": [1, 2, 3, 3],
            "count": 7,
        },
        "nil-increasing-equal-two": {
            "candies": [1, 2, 3, 3, 3],
            "count": 8,
        },
        "nil-increasing-equal-three": {
            "candies": [1, 2, 3, 3, 3, 3],
            "count": 9,
        },
        # decreasing equal
        "decreasing-equal-two-decreasing-one": {
            "candies": [4, 3, 2, 2, 1],
            "count": 9,
        },
        "decreasing-equal-two-decreasing-two": {
            "candies": [4, 3, 2, 2, 1, 0],
            "count": 12,
        },
        "decreasing-equal-two-decreasing-three": {
            "candies": [1, 2, 4, 4, 3, 2, 1, 0],
            "count": 21,
        },
        "decreasing-equal-two-increasing-one": {
            "candies": [3, 2, 1, 3],
            "count": 8,
        },
        "decreasing-equal-two-increasing-two": {
            "candies": [5, 4, 3, 3, 4, 5],
            "count": 12,
        },
        "decreasing-equal-two-increasing-three": {
            "candies": [6, 5, 3, 3, 4, 5, 6],
            "count": 16,
        },
        # decreasing increasing
        "decreasing-increasing-one-decreasing-one": {
            "candies": [4, 3, 2, 1, 2, 1],
            "count": 13,
        },
        "decreasing-increasing-2-decreasing-one": {
            "candies": [4, 3, 2, 1, 2, 3, 1],
            "count": 16,
        },
        "decreasing-increasing-one-decreasing-two": {
            "candies": [4, 3, 2, 1, 2, 1, 0],
            "count": 16,
        },
        "decreasing-increasing-2-decreasing-two": {
            "candies": [4, 3, 2, 1, 2, 3, 1, 0],
            "count": 18,
        },
        # decreasing equal
        "decreasing-equal-one-increasing-one": {
            "candies": [4, 3, 2, 1, 1, 2],
            "count": 13,
        },
        "decreasing-equal-2-increasing-one": {
            "candies": [4, 3, 2, 1, 1, 1, 3],
            "count": 14,
        },
        "decreasing-equal-one-increasing-two": {
            "candies": [4, 3, 2, 1, 1, 3, 4],
            "count": 16,
        },
        "decreasing-equal-2-increasing-two": {
            "candies": [4, 3, 2, 1, 1, 2, 3],
            "count": 16,
        },
        # increasing equal
        "increasing-equal-two-decreasing-one": {
            "candies": [1, 2, 3, 3, 2],
            "count": 9,
        },
        "increasing-equal-two-decreasing-two": {
            "candies": [1, 2, 3, 3, 2, 1],
            "count": 12,
        },
        "increasing-equal-two-decreasing-three": {
            "candies": [1, 2, 3, 3, 2, 1, 0],
            "count": 16,
        },
        "increasing-equal-two-increasing-one": {
            "candies": [1, 2, 3, 3, 4],
            "count": 9,
        },
        "increasing-equal-two-increasing-two": {
            "candies": [1, 2, 3, 3, 4, 5],
            "count": 12,
        },
        "increasing-equal-two-increasing-three": {
            "candies": [1, 2, 3, 3, 4, 5, 6],
            "count": 16,
        },
        # increasing decreasing
        "increasing-decreasing-two-equal-one": {
            "candies": [1, 2, 3, 2, 2],
            "count": 8,
        },
        "increasing-decreasing-two-equal-two": {
            "candies": [1, 2, 3, 2, 2, 2],
            "count": 9,
        },
        "increasing-decreasing-two-increasing-one": {
            "candies": [1, 2, 3, 2, 3],
            "count": 9,
        },
        "increasing-decreasing-two-increasing-two": {
            "candies": [1, 2, 3, 2, 3, 4],
            "count": 12,
        },
    }
    return items
