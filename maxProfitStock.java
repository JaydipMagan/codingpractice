/*
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find
the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

*/

class maxProfitStock{
  public static void main(String[] args) {
    int[] prices = {1,5,3,6,4};
    // int[] prices = {7,1};
    System.out.println(maxProfit(prices));
  }

  public static int maxProfit(int[] prices) {
    if(prices.length<2){
      return 0;
    }

    int max = prices[0];
    int min = prices[0];

    int indexOfMax = 0;
    int indexOfMin = 0;

    int maxProfit = 0;

    for (int i = 0 ; i<prices.length; i++) {

      System.out.println("Checking "+prices[i]);
      // check for new max
      if(prices[i]>max){
        max=prices[1];
        indexOfMax = i;
      }
      //check for new min
      if(prices[i]<min){
        min=prices[i];
        indexOfMin = i;
      }

    }
    // work out profit
    if(indexOfMax>=indexOfMin){
      System.out.println("CHECKING PROFIT");
      int profit = max-min;
      if(profit>maxProfit){
        maxProfit = profit;
      }
    }
    System.out.println(indexOfMax);
    System.out.println(indexOfMin);
    System.out.println(max);
    System.out.println(min);
    return maxProfit;
  }
}
