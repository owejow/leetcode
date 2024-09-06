# 340. Longest Substring with At Most K Distinct Characters (Hard)

Given a string you need to print longest possible substring that has exactly M
unique characters. If there is more than one substring of longest possible
length, then print any one of them.

```
Examples:

Input: Str = “aabbcc”, k = 1
Output: 2

Explanation: Max substring can be any one from {“aa” , “bb” , “cc”}.

Input: Str = “aabbcc”, k = 2
Output: 4

Explanation: Max substring can be any one from {“aabb” , “bbcc”}.

Input: Str = “aabbcc”, k = 3
Output: 6
Explanation:

There are substrings with exactly 3 unique characters
{“aabbcc” , “abbcc” , “aabbc” , “abbc” }
Max is “aabbcc” with length 6.

Input: Str = “aaabbb”, k = 3
Output: Not enough unique characters
Explanation: There are only two unique characters, thus show error message.
```

## Solutions

simple_algorithm.algorithm : contains straightforward solution

simple.algorithm : contains straightforward solution

To run tests:

python3 -m unittest ./tests/test-simple-algorithm.py
