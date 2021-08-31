package main.leetCode.easy;

public class _1221SplitAStringInBalancedStrings {
    public static int balancedStringSplit(String s) {

        int sum = 0;
        int count = 0;

        // 문자열 읽으면서 R이면 +1, L이면 -1, R과 L의 개수가 같으면 +-하여 0임.
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == 'R') {
                count++;
            } else {
                count--;
            }
            if (count == 0) {
                sum++;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(balancedStringSplit("RLRRRLLRLL"));
    }
}


/*
21.08.31 - solved

https://leetcode.com/problems/split-a-string-in-balanced-strings/

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it in the maximum amount of balanced strings.
Return the maximum amount of split balanced strings.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


Constraints:

1 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.


*/