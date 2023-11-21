class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        return x_string == x_string[::-1]


if __name__ == "__main__":
    s = Solution()

    print(s.isPalindrome(1010101))
