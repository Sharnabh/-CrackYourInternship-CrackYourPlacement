
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        ans = []

        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i] == "..":
                if ans:
                    ans.pop(-1)
            else:
                ans.append(path[i])
        path = '/'.join(ans)
        return '/'+path