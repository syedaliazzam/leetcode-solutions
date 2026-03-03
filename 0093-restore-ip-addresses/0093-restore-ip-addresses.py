class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        result = []
        
        
        def dfs(start, tlist):

            if len(tlist) == 4:
                if (start == len(s)):
                    string = ".".join(tlist)
                    result.append(string)
                return
            
            
            for end in range(start+1, len(s)+1):
                num = int(s[start:end])
                if (end-start)==2 and num <10:
                    return
                if num > 255:
                    break

                dfs(end, tlist+[str(num)])
        
        dfs(0,[])

        return result