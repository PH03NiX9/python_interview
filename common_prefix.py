# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
from ast import List


def longest_common_prefix(self, strs: List[str]) -> str:
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i ==len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res