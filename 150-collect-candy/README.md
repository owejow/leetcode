# 135. Candy (Hard)

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:

- n == ratings.length
- 1 <= n <= 2 \* 10^4
- 0 <= ratings[i] <= 2 \* 10^4

## Solutions

simple_algorithm.algorithm : contains straightforward solution using O(n) extra space
o_one_memory.algorithm : contains more complex solution with lots of edge cases requiring O(1) space.

To run tests:

python3 -m unittest ./tests/test-o-one-memory.py
python3 -m unittest ./tests/test-simple-algorithm.py
