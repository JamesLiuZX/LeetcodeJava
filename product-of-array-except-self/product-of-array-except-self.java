class Solution {
    public int[] productExceptSelf(int[] nums) {
        int sum = 1;
        int prev = nums[0];
        int[] results = new int[nums.length];
        for (int i = 1; i < nums.length ; i++){
            sum = sum * nums[i];
        }
        results[0] = sum;
        for (int i = 1; i < nums.length ; i++){
            if (nums[i] == 0){
                int newsum = 1;
                for (int j = 0; j < nums.length; j++){
                    if (j == i)continue;
                    newsum = newsum * nums[j];
                }
                prev = nums[i];
                results[i] = newsum;
                sum = newsum;
            }
            else{
            results[i] = (sum / nums[i]) * prev;
            prev = nums[i];
            sum = results[i];
            }
        }
        return results;
    }
}