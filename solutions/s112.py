"""The last number

Given a natural number, not exceeding 10000. Output its last digit.

Sample Input:
    753
Sample Output:
    3
"""


def main():
    num = input().rstrip()
    print(num[-1])

if __name__ == '__main__':
    main()
