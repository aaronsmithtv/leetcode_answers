class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_mod = x
        x_rev = 0

        while x_mod > 0:
            x_rev *= 10
            x_rev += x_mod % 10
            x_mod = x_mod // 10

        return x_rev == x


if __name__ == "__main__":
    s = Solution()

    print(s.isPalindrome(10101010))
