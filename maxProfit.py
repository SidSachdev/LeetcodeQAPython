# Leetcode MaxProfit I and II
# Buying and selling stock
# One time only


#O(n)



class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(prices):

        maxSoFar = 0
        minSoFar = float("inf")

        for num in prices:

            if num < minSoFar:

                minSoFar = num

            elif num - minSoFar > maxSoFar:

                maxSoFar = num - minSoFar

        return maxSoFar

    maxProfit([1,2,3,4,75,3,49,1])




    def multipleTransactions(prices):
        if not prices or len(prices) is 1:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return (profit)

    maxProfit([1, 2, 4])

print(Solution.multipleTransactions([1, 2, 4]))
