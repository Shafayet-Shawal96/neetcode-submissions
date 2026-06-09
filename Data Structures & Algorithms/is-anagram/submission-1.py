class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dic = dict()
        t_dic = dict()
        l = len(s)

        for i in range(l):
            if(s[i] in s_dic.keys()):
                s_dic[s[i]] = s_dic[s[i]] + 1
            else:
                s_dic[s[i]] = 1

            if(t[i] in t_dic.keys()):
                t_dic[t[i]] = t_dic[t[i]] + 1
            else:
                t_dic[t[i]] = 1

        for key in s_dic.keys():
            if(key in t_dic.keys() and s_dic[key] == t_dic[key]):
                continue
            return False

        return True



        