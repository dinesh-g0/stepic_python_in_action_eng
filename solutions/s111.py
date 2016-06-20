"""First digit of the two-digit number

Given a two-digit number. Output its first digit (i.e. the number of tens).

Sample Input:
    42
Sample Output:
    4
"""


def main():
    num = input().rstrip()
    print(num[0])

if __name__ == '__main__':
    main()
