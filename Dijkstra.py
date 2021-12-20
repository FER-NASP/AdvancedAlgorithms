from General import *
import sys

def Dijkstra(G,s,d):
    W=edges(G)
    D={}
    for v in G:
        D[v]={'d':sys.maxsize,'p':None}
    D[s]['d']=0
    work=list(D.keys())
    while work:
        work=sorted(work,key=lambda x:D[x]['d'])
        u=work.pop(0)
        if u==d:
            return D
        for v in adj(G,u):
            temp=D[u]['d']+W[(u,v)]
            if temp<D[v]['d']:
                D[v]={'d':temp,'p':u}
    return D

def DijkstraMSTUndirected(G):
    MST=NewAdjMatrix(G)
    E=edges(G)
    for e in E:
        MST[e[0]][e[1]]=MST[e[1]][e[0]]=E[e]
        c=FindCycles(MatrixToTable(MST))
        if len(c)>0:
            c=c[0]
            cp=[(c[-1],c[0])]
            for i in range(len(c)-1):
                cp.append((c[i],c[i+1]))
            E2={}
            for cpi in cp:
                E2=E2|dict(filter(lambda x:x[0][0] in cpi and x[0][1] in cpi,E.items()))
            me=max(E2.items(),key=lambda x:x[1])
            if me:
                e2=me[0]
                MST[e2[0]][e2[1]]=MST[e2[1]][e2[0]]=0
    return MST
