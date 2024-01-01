# 풀이 날짜 : 2024.01.01
# 문제 유형 : Hash Table, String, Sliding Window
# 문제 제목 : Longest Substring Without Repeating Characters
# 문제 링크 : https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 반복되는 문자열이 없는 가장 긴 substring의 길이
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 빈 문자열일 경우
        if not s:
            return 0

        lengths = []
        sub = ''

        for i, ch in enumerate(s):
            # 반복되는 문자가 없으면
            if ch not in sub:
                # sub에 더한다.
                sub += ch
                # 마지막 문자라면 그 길이를 구한다.
                if i == len(s) - 1:
                    lengths.append(len(sub))
            # 반복되는 문자가 있으면
            else:
                # 문자의 길이를 구한다.
                lengths.append(len(sub))
                # 같은 글자의 인덱스 이후의 부분만 자른 후 현재 문자를 붙인다.
                sub = sub[sub.index(ch)+1:] + ch

        return max(lengths)
