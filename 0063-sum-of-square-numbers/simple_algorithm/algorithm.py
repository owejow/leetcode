class Solution:
    def judgeSquareSum(self, c):
        """
        c: int -> bool
        """
        squares = []
        for i in range(c + 1):
            s = i * i
            if s > c:
                break
            squares.append(s)
        i = 0
        j = len(squares) - 1
        while i <= j:
            value = squares[i] + squares[j]
            if value == c:
                return True
            elif value > c:
                j -= 1
            else:
                i += 1
        return False
