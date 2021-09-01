package main.leetCode.easy;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

// 21.09.01 - solved
public class _0409LongestPalindrome {
    public static int longestPalindrome(String s) {

        // char 범위: -128 ~ +127
        int[] count = new int[128];
        int sum = s.length();
        int odd = 0;

        //아스키 코드에서 'a' -> 10진법으로 97번이므로 a[97] ~ a[100]까지 할당됨
        for (char c : s.toCharArray()) {
            // a['a'] == a[97]
            count[c]++;
        }

        for (int i = 0; i < count.length; i++) {
            if (count[i] % 2 != 0) {
                sum--;
                odd = 1;
            }
        }

        return sum + odd;

//////////////////////////////////////////////////////////////
//
//        https://leetcode.com/problems/longest-palindrome/
//         튜닝 전 코드
//
//        HashMap<Character, Integer> map = new HashMap<>();
//        int sum = s.length();
//        int add = 0;
//
//        int[] test = new int[2000];
//        for(char c : s.toCharArray()) {
//            test[c]++;
//        }
//        System.out.println(test.toString());
//
//
//        for(char c : s.toCharArray()) {
//            if(map.containsKey(c)) {
//                map.put(c, map.get(c) + 1);
//            } else {
//                map.put(c, 1);
//            }
//        }
//        Iterator it = map.entrySet().iterator();
//        while(it.hasNext()) {
//            Map.Entry<Character, Integer> entry = (Map.Entry) it.next();
//            if(entry.getValue() % 2 != 0) {
//                sum --;
//                add = 1;
//            }
//        }
//
//        return sum + add;
    }

    public static void main(String[] args) {
        System.out.println(longestPalindrome("abccccdd"));

    }
}
