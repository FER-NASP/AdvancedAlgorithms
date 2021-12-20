import collections

def adj(G,u):
    a=[]
    for v in G[u]:
        if G[u][v]!=0:
            a.append(v)
    return a

def edges(G):
    e={}
    for u in G:
        for v in adj(G,u):
            if not (v,u) in e.keys():
                e[(u,v)]=G[u][v]
    return e

def NewAdjMatrix(G,copy=False):
    am={}
    for u in G:
        am[u]={}
        for v in G[u]:
            if copy:
                am[u][v]=G[u][v]
            else:
                am[u][v]=0
    return am

def CopyAdjMatrix(G):
    return NewAdjMatrix(G,True)

def RevPath(D,d):
    P=[d]
    while D[d]['p']!=None:
        d=D[d]['p']
        P.append(d)
    return P

def RevWFI(P,s,d):
    PR=[d]
    while P[s][d]!=0:
        d=P[s][d]
        PR.append(d)
    return PR

def FindCycles(G):
    visited=[]
    cycs=[]
    S=collections.deque()
    for u0 in G:
        if u0 not in visited:
            FindCycles_r(G,u0,visited,S,cycs)
    return cycs

def FindCycles_r(G,u,visited,S,cycs):
    visited.append(u)
    S.append(u)
    for v in G[u]['adj']:
        if v not in S:
            G[v]['p']=u
            FindCycles_r(G,v,visited,S,cycs)
        else:
            if v is not G[u]['p']: # prevents turning back to the previous vertex in undirected graphs
                c = []
                for vx in reversed(S):
                    c.append(vx)
                    if vx is v:
                        break
                if c not in cycs:
                    cycs.append(c)
    S.pop()

def DetectCycle(G):
    visited=[]
    S=collections.deque()
    for u0 in G:
        if u0 not in visited:
            r=DetectCycle_r(G,u0,visited,S)
            if r: return True
    return False

def DetectCycle_r(G,u,visited,S):
    visited.append(u)
    S.append(u)
    for v in G[u]['adj']:
        if v not in S:
            G[v]['p']=u
            r=DetectCycle_r(G,v,visited,S)
            if r: return True
        else:
            if v is not G[u]['p']: # prevents turning back to the previous vertex in undirected graphs
                return True
    S.pop()
    return False

def MakeSet(F,x):
    if x not in F:
        F[x]={'p':x}
    return F

def Find(F,x):
    while F[x]['p']!=x:
        F[x]['p']=F[F[x]['p']]['p']
        x=F[x]['p']
    return x

def Union(F,x,y):
    x=Find(F,x)
    y=Find(F,y)
    F[x]['p']=y

def MatrixToTable(G):
    GR={}
    for v in G:
        GR[v]={'adj':adj(G,v)}
    return GR
