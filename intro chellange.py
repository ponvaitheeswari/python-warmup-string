def intro_sort(v,b):
    return b.index(v)
v=int(input().strip())
a=int(input().strip())
b= list(map(int, input().strip().split()))
result=intro_sort(v,b)
print(result)

'''Sample Input 0

STDIN           Function
-----           --------
4               V = 4
6               arr[] size n = 6 (not passed, see function description parameters)
1 4 5 7 9 12    arr = [1, 4, 5, 7, 9, 12]
Sample Output 0
1'''