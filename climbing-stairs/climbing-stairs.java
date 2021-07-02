class Solution {
    //Since there's only 2 ways to climb the stairs at each step, 
    //we can construct a binary tree where head of the tree 
    //head noOfWays(n) = left side noOfWays(n-1) + right side noOfWays(n-2) 
    public int climbStairs(int n) {
        if (n==1){
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i =3; i <= n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
    
}