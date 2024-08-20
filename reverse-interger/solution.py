min_value = -(2**31)
max_value = 2**31 - 1


class Solution:
    def is_outside_32bit_range(self, n):
        return n < min_value or n > max_value

    def reverse(self, x: int) -> int:
        x = str(x)
        parts = x.split("-")

        if len(parts) == 1:
            parts[0] = parts[0][::-1]
        else:
            parts[0] = "-"
            parts[1] = parts[1][::-1]

        res = int("".join(parts))
        if self.is_outside_32bit_range(res):
            return 0

        return res

# Alternative solution: 
"""
class Solution:
    def newMod(self, a, b):
        res = a % b
        return res if not res else res - b if a < 0 else res

    def reverse(self, x: int) -> int:
        new_value = 0

        while x:
            r = self.newMod(x, 10)
            new_value = new_value * 10 + r
            x = int(x / 10)

            if new_value > max_value or new_value < min_value:
                return 0

        return new_value
"""
