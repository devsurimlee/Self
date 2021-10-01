package main.leetCode.easy;

import java.util.Arrays;

public class E0561ArrayPartition1 {

    public static int arrayPairSum(int[] nums) {
        int output = 0;
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 1; i++) {
            output += nums[i];
            i++;
        }

        return output;

    }

    public static void main(String[] args) {
        int[] nums = {6, 2, 6, 5, 1, 2};
        System.out.println(arrayPairSum(nums));
    }
}

////////////////////////////////////////////
// 이전
// https://leetcode.com/problems/array-partition-i/
//
//class Solution {
//    public int arrayPairSum(int[] nums) {
//
//        int output = 0;
//        Arrays.sort(nums);
//        // sort시 홀수가 항상 min이므로 if문 필요없음
//        for (int i = 0; i < nums.length - 1; i++)
//            if (nums[i] < nums[i + 1]) {
//                output += nums[i];
//            } else {
//                output += nums[i + 1];
//            }
//            i++;
//        }
//
//        return output;
//
//
//    }
//}