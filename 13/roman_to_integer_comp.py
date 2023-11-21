class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total_value = 0
        prev_value = 0

        for character in reversed(s):
            current_value = values[character]

            if prev_value > current_value:
                current_value *= -1

            total_value += current_value
            prev_value = current_value

        return total_value


if __name__ == "__main__":
    s = Solution()

    print(s.romanToInt("MCMXCIV"))
