from math import floor, trunc
class Solution:
   def solve(self, s):
      s = list(s[::-1])

      def get_value():
         sign = 1
         if s and s[-1] == "-":
            s.pop()
            sign = -1
         value = 0
         while s and s[-1].isdigit():
            value *= 10
            value += int(s.pop())
         return sign * value

      def get_term():
         term = get_value()
         while s and s[-1] in "*/":
            op = s.pop()
            value = get_value()
            if op == "*":
               term *= value
            else:
               term = floor(1.0 * term / value)
         return term

      ans = get_term()
      while s:
         op, term = s.pop(), get_term()
         if op == "+":
            ans += term
         else:
            ans -= term
      return ans

      return ob.solve()
ob = Solution()
# s = "-12*10"
# print(ob.solve(s))
