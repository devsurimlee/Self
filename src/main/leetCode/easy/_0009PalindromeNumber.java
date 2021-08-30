package main.leetCode.easy;

public class _0009PalindromeNumber {
    public static boolean isPalindrome(int x) {
        int y = x;
        int rev = 0;
        if (x < 0) {
            return false;
        } else {
            while (y != 0) {
                int digit = y % 10;
                rev = rev * 10 + digit;
                y = y / 10;
            }
            return x == rev;

        }
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome(121));
    }
}

/*
https://leetcode.com/problems/palindrome-number/submissions/

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false


Constraints:

-231 <= x <= 231 - 1

*/