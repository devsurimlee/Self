package main.leetCode.easy;

public class E0007ReverseInteger {

    public static void main(String[] args) {

        int x = 123456789;
        int output = 0;

        String tmp = Integer.toString(x);
        String tmp2 = "";

        for (int i = tmp.length()-1; i>=0; i--) {
            if(tmp.charAt(i) != '-') {
                tmp2 += tmp.charAt(i);
            } else {
                tmp2 = "-" + tmp2;
            }
        }

        try {
            output = Integer.parseInt(tmp2);
        } catch (Exception e) {
            output = 0;
        }

        System.out.println(output);

    }
}

/*

https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
        If reversing x causes the value to go outside
        the signed 32-bit integer range [-231, 231 - 1], then return 0.

        Example 1:

        Input: x = 123
        Output: 321
        Example 2:

        Input: x = -123
        Output: -321
        Example 3:

        Input: x = 120
        Output: 21
        Example 4:

        Input: x = 0
        Output: 0
*/
