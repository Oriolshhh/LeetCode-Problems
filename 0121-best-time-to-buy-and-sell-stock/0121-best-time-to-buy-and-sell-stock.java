class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxP = 0;

        while (right < prices.length) {
            if ((prices[right] - prices[left]) > maxP) {
                maxP = prices[right] - prices[left];
            }
            if (prices[right] < prices[left]) {
                left = right;
            }
            right++;
        }

        return maxP;
    }
}
