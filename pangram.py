'''13.A pangram is a string that contains every letter of the alphabet. 
Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. 
Return either pangram or not pangram as appropriate.
Sample Input 0
We promptly judged antique ivory buckles for the next prize
Sample Output 0
pangram
Sample Explanation 0
All of the letters of the alphabet are present in the string.
Sample Input 1
We promptly judged antique ivory buckles for the prize
Sample Output 1
not pangram
Sample Explanation 0
The string lacks an x.'''
def isPangram(s):
    s = s.lower()
    letters = set()
    for char in s:
        if 'a' <= char <= 'z':
            letters.add(char)
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"
input_string = input()
result = isPangram(input_string)
print(result)