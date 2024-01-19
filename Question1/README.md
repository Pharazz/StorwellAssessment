Q1) Consider that you have a rectangular piece of paper of arbitrary dimensions N by M (where N and M are positive integers). You also have a pair of scissors which can cut perfectly straight with no loss of paper. You wish to reduce the original piece of paper into a series of perfect squares of paper, making the largest possible squares, and using all of the paper provided. Write a function in C that takes the inputs N, and M, and returns the series of squares that can be made out of that piece of paper. No fractional squares, i.e. no square should be less than 1 in length and width.

Some examples:
Input: N =6 , M = 5
Output: 5x5, 1x1, 1x1, 1x1, 1x1, 1x1

Input: N = 1, M = 1
Output: 1x1

Input: N = 9, M = 9
Output: 9x9

From the first example we see that the solution required is not to make the least amount of squares but to always create the largest square

Since in the case of N = 6 and M = 5 the least squares solution would be:

Output: 3x3, 2x2, 2x2, 1x1

Therefore the C program follows the given example to make the largest square and not the least squares
