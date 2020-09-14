class Solution:
    def calculate(self, s: str) -> int:
        x = 1
        y = 0
        for i in s:
            if i == 'A':
                x = x*2 + y
            elif i == 'B':
                y = 2*y + x
        return(x+y)
