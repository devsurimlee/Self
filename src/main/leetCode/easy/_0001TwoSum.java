package main.leetCode.easy;

import java.util.Arrays;

public class _0001TwoSum {
    public static void main(String[] args) {

        // https://leetcode.com/problems/two-sum/submissions/
        // 푸는중

        int[] output = new int[2];
        int[] nums = {2, 7, 11, 15} ;
        int target = 9;

        for(int i=0; i<nums.length; i++) {
            if(nums[i] < target) {
                output[i] = i;
            }
        }
        System.out.println(Arrays.toString(output));
    }
}
