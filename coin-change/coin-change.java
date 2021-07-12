class Solution {
    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;
        int [] dp = new int[max];
        Arrays.fill(dp,max);
        dp[0] = 0; //it takes 0 coins to have 0 dollars
        for (int i = 1; i <= dp.length - 1; i++){ //loop to fill up the memo table
            for (int j = 0; j < coins.length; j++){ //run through each coin
                //goes down the tree, result basically means (number of coins to reach the  
                //new amount if we deducted the current coin coins[j]) + 1
                if (i >= coins[j]){ //skip loop if current amount is less than current coin
                    int result = dp[i - coins[j]] + 1;       
                    if (result < dp[i]){
                        dp[i] = result; //store least number of coins needed into dp[i]
                    }
                }
            }
        }
        return dp[amount] <= amount ? dp[amount] :-1; //catches case where there is no solution
    }
}
    
