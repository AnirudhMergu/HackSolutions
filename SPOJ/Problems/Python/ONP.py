"""
ONP - Transform the Expression

Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation).
Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ).
Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).

Input
t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
Text grouped in [ ] does not appear in the input file.

Output
The expressions in RPN form, one per line.
Example
Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*

Author : Anirudh Sai Mergu
Website: www.anirudhmergu.com
Question URL: http://www.spoj.com/problems/PRIME1/
"""

from sys import stdin


def main():
    itr = int(input())

    for i in range(itr):
        string = input()

        priority = {'(': 1, ')': 1, '^': 5, '*': 3, '/': 4, '+': 1, '-': 2}
        stack = []

        for x in range(len(string)):
            if string[x] in priority.keys():
                if len(stack) == 0:
                    stack += string[x]
                else:
                    if string[x] == ')':
                        if len(stack) != 0:
                            while stack[len(stack) - 1] != '(':
                                print(stack.pop(), end="")
                            stack.pop()

                    elif string[x] == '(':
                        stack += string[x]

                    elif priority[string[x]] > priority[stack[-1]]:
                        stack += string[x]

                    else:
                        if len(stack) - 1 != 0 and stack[len(stack) - 1] != '(':
                            print(stack.pop(), end="")
                            stack += string[x]
                        else:
                            stack += string[x]
            else:
                print(string[x], end="")

        while len(stack) != 0:
            print(stack.pop(), end="")
        print()


try:
    main()
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
