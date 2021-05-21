class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i1 = self.nextValidChar(s, i)
            j1 = self.nextValidChar(t, j)
            
            if i1 < 0 and j1 < 0:
                return True
            if i1 < 0 or j1 < 0:
                return False
            if s[i1] != t[j1]:
                return False
            
            i = i1 - 1
            j = j1 - 1
        return True
    
    def nextValidChar(self, st, index):
        count = 0
        while index >= 0:
            if st[index] == '#':
                count += 1
            elif count > 0:
                count -= 1
            else:
                break
            index -= 1
        return index
