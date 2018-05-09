"""
Complete the function solveMeFirst to compute the sum of two integers.

Function prototype:

int solveMeFirst(int x, int y);

where,

x is the first integer input.
y is the second integer input
Return values

sum of the above two integers
Sample Input

x = 2
y = 3
Sample Output

5
Explanation

The sum of the two integers x and y is computed as: 2 + 3 = 5.

Author : Anirudh Sai Mergu
Website: www.anirudhmergu.com
Question URL: http://www.spoj.com/problems/PRIME1/
"""


def solve_me_first(a, b):
    # Hint: Type return a+b below
    return a + b


def main():
    num1 = int(input())
    num2 = int(input())
    res = solve_me_first(num1, num2)
    print(res)


try:
    main()
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
