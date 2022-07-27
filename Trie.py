class TrieNode:
    def __init__(self,p=None):
        self.children={}
        self.parent=p
    def isLeaf(self) -> (bool):
        return len(self.children)==0
    def transition(self,c:chr) -> (bool,object):
        if c in self.children: return (True,self.children[c])
        return (False,None)
    def insert(self,c:chr) -> (object):
        (ct,cn)=self.transition(c)
        if not ct:
            ncn=TrieNode(self)
            self.children[c]=ncn
            return ncn
        else: return cn
    def remove(self,c:chr) -> (bool):
        (ct,cn)=self.transition(c)
        if ct:
            del self.children[c]
            return True
        return False

class Trie:
    def __init__(self):
        self.root=TrieNode(None)
    def insert(self,s:str):
        currTN=self.root
        for c in s:
            currTN=currTN.insert(c)
        currTN.insert('$')
    def search(self,q:str) -> (bool,TrieNode):
        currTN=self.root
        for c in q+'$':
            (res,currTN)=currTN.transition(c)
            if not res: return (False,currTN)
        return (currTN.isLeaf(),currTN)
    def remove(self,s:str) -> (bool):
        (res,ltn)=self.search(s)
        if res:
            s='$'+"".join(reversed(s))
            currTN=ltn.parent
            for c in s:
                split=len(currTN.children)>1
                currTN.remove(c)
                if split: break
                currTN=currTN.parent
                if currTN is None: break
            return True
        return False
