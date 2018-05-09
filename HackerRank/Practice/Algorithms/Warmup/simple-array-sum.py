"""
Given an array of integers, find the sum of its elements.

Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers representing the
array's elements.

Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11
Sample Output

31
Explanation

We print the sum of the array's elements: .

Author : Anirudh Sai Mergu
Website: www.anirudhmergu.com
Question URL: https://www.hackerrank.com/challenges/simple-array-sum/problem
"""
import os


def simpleArraySum(ar):
    #
    # Write your code here.
    #
    return sum(ar)


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


try:
    main()
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
