"""Leap year

The problem is to find whether the given year is a leap year.

Just a reminder: leap years are those years, the number of which is either
divisible by 4, but not divisible by 100, or divisible by 400 (for example,
the year 2000 is a leap year, but the year 2100 will not be a leap year).

The program should work correctly for the years 1900 ≤ n ≤ 3000.

Output "Leap" (case-sensitive) if the given year is a leap, and "Regular"
otherwise.

Sample Input 1:
    2100
Sample Output 1:
    Regular

Sample Input 2:
    2000
Sample Output 2:
    Leap
"""


def main():
    year = int(input().rstrip())

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Leap')
    else:
        print('Regular')

if __name__ == '__main__':
    main()
