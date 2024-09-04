# 125. Valid Palindrome

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

```
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

```
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

```

## Solutions

simple_algorithm.algorithm : contains straightforward solution

o_1_space.algorithm : contains algorithm with o(1) space

simple.algorithm : contains straightforward solution
