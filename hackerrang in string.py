'''12.Function Description
Complete the hackerrankInString function in the editor below.
hackerrankInString has the following parameter(s):
string s: a string
Returns
string: YES or NO
Input Format
The first line contains an integer q, the number of queries.
Each of the next q lines contains a single query string s.
Sample Input 0
2
hereiamstackerrank
hackerworld
Sample Output 0
YES
NO
Explanation 0
We perform the following q=2  queries:
1.s=hereiamstackerrank
The characters of hackerrank are bolded in the string above. Because 
the string contains all the characters in 
hackerrank in the same exact order as they appear in hackerrank, we return YES.
2.s=hackerworld does not contain the last three characters of hackerrank, so we return NO.'''
def containsString(s, sub):
    i = 0
    j = 0
    while i < len(s) and j < len(sub):
        if s[i] == sub[j]:
            j += 1
        i += 1
    if j == len(sub):
        return "YES"
    else:
        return "NO"
q = int(input())
queries = []
for _ in range(q):
    s = input().strip()
    queries.append(s)
sub = "hackerrank"
for string in queries:
    result = containsString(string, sub)
    print(result)