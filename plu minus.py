'''15.Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each 
fraction on a new line with 6 places after the decimal.
Print
Print the ratios of positive, negative and zero values in the array. 
Each value should be printed on a separate line with 6 digits after the decimal. 
The function should not return a value.
ample Input
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output
0.500000
0.333333
0.166667
Explanation
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive:3/6=0.500000 , negative:2/6=0.333333
  and zeros:1/6=0.166667 .'''
def plusMinus(arr):
    n = len(arr)
    positive_count = sum(x > 0 for x in arr)
    negative_count = sum(x < 0 for x in arr)
    zero_count = sum(x == 0 for x in arr)
    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
n = int(input())
arr = list(map(int, input().split()))
plusMinus(arr)