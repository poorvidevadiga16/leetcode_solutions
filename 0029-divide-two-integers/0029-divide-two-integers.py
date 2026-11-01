
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend = dividend - temp
            result = result + multiple

        if sign < 0:
            result = -result

        return max(-2147483648, min(result, 2147483647))

        