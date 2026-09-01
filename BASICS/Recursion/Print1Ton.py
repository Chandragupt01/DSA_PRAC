class solution:
    def print1ton(self, n):
        if n == 0:
            return
        self.print1ton(n-1)
        print(n)

sol = solution()
sol.print1ton(5)

# class Solution:
#     # Recursive function to print numbers from current to n using backtracking
#     def printNumbers(self, current, n):
#         # Base case: if current exceeds n, stop recursion
#         if current > n:
#             return

#         # Recursive call with next number
#         self.printNumbers(current + 1, n)

#         # Print current number during backtracking
#         print(current, end=' ')