'''10.Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:
Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?
Note: Here's the set of types of characters in a form you can paste in your solution:
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
Example
password='2bbbb'
This password is 5 characters long and is missing an uppercase and a special
 character. The minimum number of characters to add is 2.
password='2bb#A'
This password is 5 characters long and has at least one of each character type. 
The minimum number of characters to add is 2.
Function Description
Complete the minimumNumber function in the editor below.
minimumNumber has the following parameters:
int n: the length of the password
string password: the password to test
Returns
int: the minimum number of characters to add
Input Format
The first line contains an integer n , the length of the password.
The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.
Constraints
1<=n<=100
All characters in password are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].
Sample Input 0
3
Ab1
Sample Output 0
3
Explanation 0
She can make the password strong by adding 3 characters, for example, $hk, turning the password into Ab1$hk which is strong.
2 characters aren't enough since the length must be at least 6.
Sample Input 1
11
#HackerRank
Sample Output 1
1
Explanation 1
The password isn't strong, but she can make it strong by adding a single digit.'''
def minimumNumber(n, password):
    count = 0
    conditions = [False] * 4
    for char in password:
        if char.isdigit():
            conditions[0] = True
        elif char.islower():
            conditions[1] = True
        elif char.isupper():
            conditions[2] = True
        elif char in "!@#$%^&*()-+":
            conditions[3] = True
    for cond in conditions:
        if not cond:
            count += 1
    if n < 6 and count + n < 6:
        count += 6 - (count + n)
    return count
n = int(input())
password = input()
result = minimumNumber(n, password)
print(result)