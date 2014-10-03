import unittest


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        # subproblem is maxProduct(A[n-1])
        # looks like optimal substructrure, dp should be applicable
        #
        # let's use:
        #   m: positive product for A[x:i], initial with 0
        #   n: negative product for A[x:i], initial with 0
        #
        # for example [2,3,-2,4]
        # i     2    3   -2   4
        # m     2    6    0   4
        # n     0    0   -12  -48
        # best  2    6    6   6
        if not A:
            raise ValueError
        if len(A) == 1:
            return A[0]

        m, n, best = 0, 0, float('-inf')
        for i in A:
            if i >= 0:
                m, n = max(m * i, i), n * i
            else:
                m, n = n * i, min(m * i, i)
            best = max(m, best)
        return best



class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.maxProduct([-2,0,-1]), 0)
        self.assertEqual(s.maxProduct([-4,-3,-2]), 12)
        self.assertEqual(s.maxProduct([2,3,-2,4]), 6)
        self.assertEqual(s.maxProduct([-2]), -2)
        self.assertEqual(s.maxProduct([0.1, 0.1, 2]), 2)
        self.assertEqual(s.maxProduct([-2, 2, -2]), 8)
        self.assertEqual(s.maxProduct([0, -2, 4]), 4)
        self.assertEqual(s.maxProduct([0, -2, -2, 4]), 16)
        self.assertEqual(s.maxProduct([1, -2, 2, 2, 4]), 16)


if __name__ == '__main__':
    unittest.main()
