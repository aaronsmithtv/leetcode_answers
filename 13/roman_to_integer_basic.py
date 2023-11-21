class Solution:
    def romanToInt(self, s: str) -> int:
        conditions = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        s_cull = s
        total_value = 0

        for key, value in conditions.items():
            if key in s:
                s_cull = s_cull.replace(key, '')
                total_value += value

        for character in s_cull:
            total_value += values[character]

        return total_value

if __name__ == "__main__":
    s = Solution()

    print(s.romanToInt("MCMXCIV"))