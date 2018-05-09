"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale
from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A = (a[0],a[1],a[2]),
and the rating for Bob's challenge to be the triplet B = (b[0],b[1],b[2]).

Your task is to find their comparison points by comparing a[0] with b[0],a[1] with b[1],
and b[1] with b[2].

If a[i]>b[i], then Alice is awarded  point.
If a[i]<b[i], then Bob is awarded  point.
If a[i]=b[i], then neither person receives a point.
Comparison points is the total points a person earned.

Given A and B, can you compare the two challenges and print their respective comparison points?

Input Format

The first line contains  space-separated integers, a[0], a[1], and a[2], describing the respective values in triplet A.
The second line contains  space-separated integers, b[0], b[1], and b[2], describing the respective values in triplet B.

Constraints
* 1<=a[i]<=100
* 1<=b[i]<=100
Output Format

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

Sample Input

5 6 7
3 6 10
Sample Output

1 1
Explanation
Visit on HackerRank

Author : Anirudh Sai Mergu
Website: www.anirudhmergu.com
Question URL: https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""
# !/bin/python3

import os
import sys


#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    aPoints = 0
    bPoints = 0

    if a0 > b0:
        aPoints += 1
    elif a0 < b0:
        bPoints += 1

    if a1 > b1:
        aPoints += 1
    elif a1 < b1:
        bPoints += 1

    if a2 > b2:
        aPoints += 1
    elif a2 < b2:
        bPoints += 1

    return str(aPoints) + str(bPoints)


def main():
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    result = solve(a[0], a[1], a[2], b[0], b[1], b[2])

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()


try:
    main()
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
