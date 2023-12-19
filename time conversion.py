'''8.Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
Example
s='12:01:00pm
Return '12:01:00'.
s='12:01:00am
Return '00:01:00'.
Function Description
Complete the timeConversion function in the editor below. It should 
return a new string representing the input time in 24 hour format.
timeConversion has the following parameter(s):
string s: a time in 12 hour format
Returns
string: the time in 24 hour format
Input Format
A single string  that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).
Constraints
All input times are valid
Sample Input 0
07:05:45PM
Sample Output 0
19:05:45'''
def timeConversion(s):
    hour, minute, second = map(int, s[:-2].split(':'))
    meridiem = s[-2:]
    if meridiem == 'PM' and hour != 12:
        hour += 12
    elif meridiem == 'AM' and hour == 12:
        hour = 0
    return '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)
s = input().strip()
result = timeConversion(s)
print(result)