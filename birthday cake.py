'''7.You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
Example
candle=[4,4,1,3]
The maximum height candles are 4 units high. There are 2 of them, so return 2.
Function Description
Complete the function birthdayCakeCandles in the editor below.
birthdayCakeCandles has the following parameter(s):
int candles[n]: the candle heights
Returns
int: the number of candles that are tallest
Input Format
The first line contains a single integer, n , the size of candle.
The second line contains n space-separated integers, where each integer  describes 
the height of candles[i].
Constraints
1<=n<=10^5
1<=candles[i]<=10^7
Sample Input 0
4
3 2 1 3
Sample Output 0
2
Explanation 0
Candle heights are[3,2,1,3] . The tallest candles are 3 units, and there are 2 of 
them.'''
def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count
n = int(input())
candles = list(map(int, input().split()))
result = birthdayCakeCandles(candles)
print(result)