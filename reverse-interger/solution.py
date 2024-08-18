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
