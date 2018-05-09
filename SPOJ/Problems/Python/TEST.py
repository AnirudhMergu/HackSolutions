"""
TEST - Life, the Universe, and Everything

Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything.
More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42.
All numbers at input are integers of one or two digits.


Example
Input:
1
2
88
42
99

Output:
1
2
88
Information
In case of any problems with your code, you can take a look in the forum, you'll find the answer,
only for this problem, in various languages.

Author : Anirudh Sai Mergu
Website: www.anirudhmergu.com
Question URL: http://www.spoj.com/problems/TEST/
"""


# your code goes here
def main():
    while True:
        inp = int(input().strip())
        if inp == 42:
            break
        print(inp)


try:
    main()
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
