class PatriciaTreeNode:
    def __init__(self, s: str, p: int, l: int):
        self.s, self.p, self.l = s, p, l
        self.children = []
    def isLeaf(self) -> (bool):
        return len(self.children) == 0
    def __str__(self):
        return self.s[self.p:self.p+self.l]


class PatriciaTree:
    def __init__(self):
        self.root = PatriciaTreeNode('', 0, 0)
    def search(self, q: str):
        q = q + '$'
        q_p, q_l = 0, len(q)
        sc = 0  # Python starts strings from 0
        cn = self.root
        while not cn.isLeaf():
            cmatch = False
            for cnc in cn.children:
                t_p, t_l = cnc.p, cnc.l
                if q[sc:sc + t_l] == cnc.s[t_p:t_p + t_l]:
                    sc, cn = sc + t_l, cnc
                    cmatch = True
                    break
            if not cmatch: return False
        return sc == q_l
    def insert(self, s: str):
        s=s+'$'
        s_p, s_l = 0, len(s)
        sc = 0 # Python starts strings from 0
        cn = self.root
        while not cn.isLeaf():
            nfound = True
            for cnc in cn.children:
                case = 3
                t_p, t_l = cnc.p, cnc.l
                for i in range(0, t_l):
                    if s[sc + i] != cnc.s[cnc.p + i]:
                        if i == 0: case = 1
                        else: case = 2
                        break
                if case == 3:
                    cn,sc=cnc,sc+t_l
                    nfound=False
                    break
                elif case == 2:
                    cn.children.remove(cnc)
                    cnins=PatriciaTreeNode(cnc.s,cnc.p,i)
                    cnc.p,cnc.l=cnc.p+i,cnc.l-i
                    cn.children.append(cnins)
                    cnins.children.append(cnc)
                    cnleaf=PatriciaTreeNode(s,sc+i,s_l-sc-i)
                    cnins.children.append(cnleaf)
                    return
            if nfound: break
        if sc<s_l:
            cnleaf=PatriciaTreeNode(s,sc,s_l-sc)
            cn.children.append(cnleaf)



