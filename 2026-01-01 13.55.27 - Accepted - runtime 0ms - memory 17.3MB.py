class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_len = 0
        zeros = 0
        ones = 0
        
        for c in s:
            if c == '0':
                if ones > 0:  # Reset when we see 0 after seeing 1
                    zeros = 0
                    ones = 0
                zeros += 1
            else:  # c == '1'
                ones += 1
                # Update max length: balanced means min(zeros, ones) pairs
                max_len = max(max_len, 2 * min(zeros, ones))
        
        return max_len