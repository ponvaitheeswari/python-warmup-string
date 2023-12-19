def funnyString(s):
    # Create a reversed copy of the string
    reversed_s = s[::-1]
    
    # Calculate ASCII differences for the original and reversed strings
    ascii_diff_s = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)]
    ascii_diff_reversed_s = [abs(ord(reversed_s[i]) - ord(reversed_s[i + 1])) for i in range(len(reversed_s) - 1)]

    # Check if the ASCII difference lists are the same
    if ascii_diff_s == ascii_diff_reversed_s:
        return "Funny"
    else:
        return "Not Funny"

# Reading input values
q = int(input())
queries = []
for _ in range(q):
    s = input().strip()
    queries.append(s)

# Checking if each string in the queries list is funny or not
for string in queries:
    result = funnyString(string)
    print(result)