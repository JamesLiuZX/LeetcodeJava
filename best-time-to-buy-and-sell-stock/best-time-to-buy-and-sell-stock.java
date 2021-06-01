class Solution {
    public int maxProfit(int[] prices) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++){
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }
}


/* 
a less efficient O(N^2) solution
class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        for (int i = 0; i < prices.length; i++){
            for (int j = i + 1; j < prices.length; j++){
                if (prices[j] - max > prices[i])
                    max = prices[j] - prices[i];
            }
        }
        return max;
    }
}
*/