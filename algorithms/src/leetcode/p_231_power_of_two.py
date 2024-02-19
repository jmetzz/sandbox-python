"""
https://leetcode.com/problems/power-of-two/description

231. Power of Two
Easy

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
-231 <= n <= 231 - 1


Follow up: Could you solve it without loops/recursion?
"""

import numpy


class PowerOfTwo:
    def solve_mathematically(self, n: int) -> bool:
        return float.is_integer(numpy.log2(n))

    def solve_loop(self, n) -> bool:
        if n == 0:
            return False

        while n % 2 == 0:
            n /= 2
        return n == 1

    def solve_bitwise(self, n: int) -> bool:
        """
        Examples
            3->0000 0011 --> False
            2->0000 0010 --> True
            4->0000 0100 --> True
            5->0000 0101 --> False
            6->0000 0110 --> False
            7->0000 0111 --> False
            8->0000 1000 --> True

            For all True cases, only one active bit exists:
                4->0000 0100
                8->0000 1000

            bit(7) -> 0111
            bit(8) -> 1000
            bit(7 & 8) -> 0000

        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
