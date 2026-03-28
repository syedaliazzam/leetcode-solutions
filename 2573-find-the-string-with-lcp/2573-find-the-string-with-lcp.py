class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        max_alpha = ord('a')
        groups = list(range(n))
        not_equal = []
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(i + 1, n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if i > 0 and ((lcp[i-1][j-1] > 0 and lcp[i][j] != lcp[i-1][j-1] - 1)):
                    return ""
                if lcp[i][j] > n - i or lcp[i][j] > n - j:
                    return ""
                if lcp[i][j] > 0:
                    if groups[j] != j and groups[j] != groups[i]:
                        return ""
                    groups[j] = groups[i]
                else:
                    not_equal.append((i, j))
        assignments = {}
        s = []
        for v in groups:
            if v not in assignments:
                assignments[v] = chr(max_alpha)
                if not assignments[v].isalpha():
                    return ""
                max_alpha += 1
            s.append(assignments[v])
        if any(s[i] == s[j] for i, j in not_equal):
            return ""        
        return "".join(s)