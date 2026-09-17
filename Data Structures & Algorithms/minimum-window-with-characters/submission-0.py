from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        left = 0
        right = 0

        have = 0
        need_count = len(need)

        result = ""
        result_length = float("inf")

        while right < len(s):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                window_length = right - left + 1

                if window_length < result_length:
                    result_length = window_length
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

            right += 1

        return result