# 다시풀기!

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        if (citations[0] == 0):
            return 0
        if citations[-1] >= len(citations):
            return len(citations)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return 0
