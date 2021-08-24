package main.leetCode.easy;

import java.util.Arrays;

/*
        https://leetcode.com/problems/two-sum/submissions/

        Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].
        Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]
*/


public class _0001TwoSum {
    public static void main(String[] args) {

        int[] output = new int[2];
        int[] nums = {3, 2, 4} ;
        int target = 6;

        // 이중 for문으로 앞+뒤 숫자 더해서 target이랑 같은지 찾음
        for(int i=0; i<nums.length; i++) {
            for(int j=i+1; j<nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    output[0] = i;
                    output[1] = j;
                    break;
                }
            }
        }
        System.out.println(Arrays.toString(output));
    }
}
