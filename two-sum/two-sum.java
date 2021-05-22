class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] results = new int[2];
        if (nums.length == 2){
            results[0] = 0;
            results[1] = 1;
        }
        else{
            for (int i = 0; i < nums.length; i ++){
            for (int j = i + 1; j < nums.length; j ++){
                if (nums[i] + nums[j] == target){
                    results[0] = i;
                    results[1] = j;
                }
            }
            }
        }return results;
    }   
}