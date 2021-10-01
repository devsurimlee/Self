package main.leetCode.easy;

public class E0680ValidPalindrome2 {

    public static boolean validPalindrome(String s) {

        int right = s.length() - 1;

        // 문자열 양끝부터 스캔, 중앙에서 멈춤
        for (int left = 0; left < right; left++) {
            // 서로 다른 문자 발견시 한칸씩 땡겨서 중앙까지 스캔, 서로 다른 문자 또 발견시 2번 이상이므로 false 처리
            if (s.charAt(left) != s.charAt(right)) {
                return isPalindrome(left+1, right, s) || isPalindrome(left, right -1, s);
            }
            right--;
        }
        return true;

    }

    public static boolean isPalindrome(int left, int right, String s) {

        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }


    public static void main(String[] args) {

        String s = "eeccccbebaeeabebccceea";
        System.out.println(validPalindrome(s));

    }
}

///////////////////////////////////////////////////////////
//
// https://leetcode.com/problems/valid-palindrome-ii/
// 못풀어서 해당 풀이보고 개선해봄
//      https://leetcode.com/problems/valid-palindrome-ii/discuss/493705/Java-Iterative-Solution-in-O(n)-time-or-Easy-to-read
//
//