'''1.Complete the function solveMeFirst to compute the sum of two integers.
Example
a=7
b=3
retrun 10
Function Description
Complete the solveMeFirst function in the editor below.
solveMeFirst has the following parameters:
int a: the first value
int b: the second value
Returns
int: the sum of a and b
Sample Input
a = 2
b = 3
Sample Output
5
Explanation
 2+3=5'''
def sum(n1,n2):
    sum2=n1+n2
    return (sum2)
a=int(input())
b=int(input())
result=sum(a,b)
print(result)