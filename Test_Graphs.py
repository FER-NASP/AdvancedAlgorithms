import unittest
from TwoMSTTravelingSalesman import TwoMSTTSP
from BellmanFord import BellmanFord,BellmanFordFast
from General import RevPath,FindCycles,GenerateRandomMatrix,RevWFI,GenerateRandomCompleteUndirectedGraph,FindCycleWithWeightsMatrix
from BFS_Iterative import BFS
from BlockSearch import BlockSearch
from DFS import DFS,DFSIterative
from Dijkstra import Dijkstra,DijkstraMSTUndirected,DijkstraMSTUndirectedMatrix
from EdmondsKarp import EdmondsKarp
from EulerianCircuits import Fleury,Hierholzer,Eulerization,IsEulerianCircuit
import copy
from Kruskal import KruskalUndirected
from Prim import Prim
from SCCSearch import SCCSearch
from WFI import WFI
from random import randint

class SimpleBinaryTreeCases(unittest.TestCase):
    def test_2MSTTS(self):
        # G= {'A': {'A':0,'B':1,'C':5,'D':4,'E':7,'F':4,'G':2},
        #     'B': {'A':1,'B':0,'C':4,'D':5,'E':7,'F':1,'G':4},
        #     'C': {'A':5,'B':4,'C':0,'D':2,'E':4,'F':5,'G':1},
        #     'D': {'A':4,'B':5,'C':2,'D':0,'E':7,'F':5,'G':4},
        #     'E': {'A':7,'B':7,'C':4,'D':7,'E':0,'F':2,'G':4},
        #     'F': {'A':4,'B':1,'C':5,'D':5,'E':2,'F':0,'G':8},
        #     'G': {'A':2,'B':4,'C':1,'D':4,'E':4,'F':8,'G':0}}
        #
        # G= {'A': {'A':0,'B':3,'C':4,'D':5,'E':4,'F':8,'G':1},
        #     'B': {'A':3,'B':0,'C':6,'D':4,'E':7,'F':9,'G':5},
        #     'C': {'A':4,'B':6,'C':0,'D':3,'E':7,'F':8,'G':4},
        #     'D': {'A':5,'B':4,'C':3,'D':0,'E':4,'F':6,'G':3},
        #     'E': {'A':4,'B':7,'C':7,'D':4,'E':0,'F':2,'G':2},
        #     'F': {'A':8,'B':9,'C':8,'D':6,'E':2,'F':0,'G':8},
        #     'G': {'A':1,'B':5,'C':4,'D':3,'E':2,'F':8,'G':0}}
        #
        # G= {'A': {'A':0,'B':4,'C':1,'D':5,'E':7,'F':6,'G':4},
        #     'B': {'A':4,'B':0,'C':10,'D':9,'E':3,'F':5,'G':1},
        #     'C': {'A':1,'B':10,'C':0,'D':1,'E':4,'F':4,'G':5},
        #     'D': {'A':5,'B':9,'C':1,'D':0,'E':5,'F':7,'G':3},
        #     'E': {'A':7,'B':3,'C':4,'D':5,'E':0,'F':2,'G':4},
        #     'F': {'A':6,'B':5,'C':4,'D':7,'E':2,'F':0,'G':9},
        #     'G': {'A':4,'B':1,'C':5,'D':3,'E':4,'F':9,'G':0}}

        # G= {'A': {'A':0,'B':5,'C':8,'D':3,'E':4,'F':4,'G':10},
        #     'B': {'A':5,'B':0,'C':2,'D':9,'E':5,'F':6,'G':6},
        #     'C': {'A':8,'B':2,'C':0,'D':1,'E':8,'F':7,'G':5},
        #     'D': {'A':3,'B':9,'C':1,'D':0,'E':2,'F':5,'G':4},
        #     'E': {'A':4,'B':5,'C':8,'D':2,'E':0,'F':9,'G':3},
        #     'F': {'A':4,'B':6,'C':7,'D':5,'E':9,'F':0,'G':1},
        #     'G': {'A':10,'B':6,'C':5,'D':4,'E':3,'F':1,'G':0}}

        # G= {'A': {'A':0,'B':5,'C':5,'D':2,'E':1,'F':4,'G':7},
        #     'B': {'A':5,'B':0,'C':9,'D':6,'E':4,'F':4,'G':2},
        #     'C': {'A':5,'B':9,'C':0,'D':9,'E':6,'F':5,'G':2},
        #     'D': {'A':2,'B':6,'C':9,'D':0,'E':7,'F':4,'G':5},
        #     'E': {'A':1,'B':4,'C':6,'D':7,'E':0,'F':1,'G':3},
        #     'F': {'A':4,'B':4,'C':5,'D':4,'E':1,'F':0,'G':9},
        #     'G': {'A':7,'B':2,'C':2,'D':5,'E':3,'F':9,'G':0}}

        G= {'A': {'A':0,'B':5,'C':4,'D':7,'E':2,'F':9,'G':3},
            'B': {'A':5,'B':0,'C':1,'D':4,'E':7,'F':8,'G':5},
            'C': {'A':4,'B':1,'C':0,'D':2,'E':7,'F':7,'G':4},
            'D': {'A':7,'B':4,'C':2,'D':0,'E':2,'F':5,'G':4},
            'E': {'A':2,'B':7,'C':7,'D':2,'E':0,'F':1,'G':7},
            'F': {'A':9,'B':8,'C':7,'D':5,'E':1,'F':0,'G':6},
            'G': {'A':3,'B':5,'C':4,'D':4,'E':7,'F':6,'G':0}}
        #G= {'A':{'A':0,'B':1,'C':1,'D':4},
        #    'B':{'A':1,'B':0,'C':4,'D':5},
        #    'C':{'A':1,'B':4,'C':0,'D':2},
        #    'D':{'A':4,'B':5,'C':2,'D':0}}
        Ch=TwoMSTTSP(G,'A')
        print(Ch)
        self.assertTrue((('a','e'),2) in Ch,len(Ch)==5)

    def test_BellmanFord(self):
        G= {'a': {'a':0,'b':1,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0},
            'b': {'a':0,'b':0,'c':0,'d':0,'e':-5,'f':0,'g':0,'h':0,'i':0},
            'c': {'a':0,'b':0,'c':0,'d':1,'e':0,'f':0,'g':1,'h':1,'i':0},
            'd': {'a':2,'b':0,'c':0,'d':0,'e':4,'f':0,'g':0,'h':0,'i':1},
            'e': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':4,'g':0,'h':0,'i':0},
            'f': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0},
            'g': {'a':0,'b':0,'c':0,'d':-1,'e':0,'f':0,'g':0,'h':0,'i':0},
            'h': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':-1,'h':0,'i':0},
            'i': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':1,'g':0,'h':0,'i':0}
            }
        D1=BellmanFord(G,'c')
        D2=BellmanFordFast(G,'c')
        self.assertTrue(RevPath(D1,'f')==['f', 'i', 'd', 'g', 'h', 'c'],RevPath(D2,'f')==['f', 'i', 'd', 'g', 'h', 'c'])

    def test_BFSIterative(self):
        G = {}
        G['a'] = {'adj':['b','c','d']}
        G['b'] = {'adj':['a','e','f']}
        G['c'] = {'adj':['a','f']}
        G['d'] = {'adj':['a','h']}
        G['e'] = {'adj':['b','i']}
        G['f'] = {'adj':['b','c','g']}
        G['g'] = {'adj':['f','i']}
        G['h'] = {'adj':['d','i']}
        G['i'] = {'adj':['e','g','h']}
        self.assertTrue(BFS(G)==['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'g'])

    def test_BlockSearch(self):
        G = {}
        #G['a'] = {'adj':['c']}
        #G['b'] = {'adj':[]}
        #G['c'] = {'adj':['b','d','e','f']}
        #G['d'] = {'adj':['c','e','f']}
        #G['e'] = {'adj':['c','d','f']}
        #G['f'] = {'adj':['c','d','e']}
        G['a'] = {'adj':['c','d','f']}
        G['c'] = {'adj':['a','f']}
        G['f'] = {'adj':['a','c','d']}
        G['d'] = {'adj':['a','b','e']}
        G['b'] = {'adj':['d','e','g','h']}
        G['e'] = {'adj':['b','d']}
        G['g'] = {'adj':['b','h','k']}
        G['h'] = {'adj':['b','g','i','k']}
        G['i'] = {'adj':['h','j']}
        G['j'] = {'adj':['i']}
        G['k'] = {'adj':['g','h']}
        G['l'] = {'adj':['m']}
        G['m'] = {'adj':['l']}
        blocks=BlockSearch(G)
        #print(blocks)

    def test_DFS(self):
        G = {}
        G['a'] = {'adj':['b','c','d']}
        G['b'] = {'adj':['a','e','f']}
        G['c'] = {'adj':['a','f']}
        G['d'] = {'adj':['a','h']}
        G['e'] = {'adj':['b','i']}
        G['f'] = {'adj':['b','c','g']}
        G['g'] = {'adj':['f','i']}
        G['h'] = {'adj':['d','i']}
        G['i'] = {'adj':['e','g','h']}
        r1=DFSIterative(G)
        #print(r1)
        r2=DFS(G)
        #print(r2)

    def test_Dijkstra(self):
        G= {'a': {'a':0,'b':0,'c':0,'d':0,'e':1,'f':0,'g':0,'h':10,'i':0,'j':0},
            'b': {'a':0,'b':0,'c':2,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0},
            'c': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0},
            'd': {'a':4,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':1,'i':0,'j':0},
            'e': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':3,'g':0,'h':0,'i':0,'j':0},
            'f': {'a':0,'b':1,'c':3,'d':0,'e':0,'f':0,'g':7,'h':0,'i':1,'j':0},
            'g': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0},
            'h': {'a':0,'b':0,'c':0,'d':0,'e':5,'f':0,'g':0,'h':0,'i':9,'j':0},
            'i': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':2},
            'j': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':1,'h':0,'i':0,'j':0}
            }
        D=Dijkstra(G,'d','g')
        DRP=RevPath(D,'g')
        print(DRP)
        #G2={'a': {'a':0,'b':6,'c':5,'d':0,'e':0,'f':0,'g':0},
        #    'b': {'a':6,'b':0,'c':9,'d':0,'e':13,'f':0,'g':0},
        #    'c': {'a':5,'b':9,'c':0,'d':16,'e':0,'f':12,'g':0},
        #    'd': {'a':0,'b':0,'c':16,'d':0,'e':15,'f':7,'g':0},
        #    'e': {'a':0,'b':13,'c':0,'d':15,'e':0,'f':0,'g':8},
        #    'f': {'a':0,'b':0,'c':12,'d':7,'e':0,'f':0,'g':3},
        #    'g': {'a':0,'b':0,'c':0,'d':0,'e':8,'f':3,'g':0}}
        G={'a':{'a':0, 'b':2, 'c':3, 'd':0},
            'b':{'a':2, 'b':0, 'c':5, 'd':0},
            'c':{'a':3, 'b':5, 'c':0, 'd':0},
            'd':{'a':0, 'b':0, 'c':0, 'd':0}}
        print(FindCycleWithWeightsMatrix(G))
        G2={'a':{'a':0, 'b':2, 'c':5, 'd':6},
            'b':{'a':2, 'b':0, 'c':3, 'd':4},
            'c':{'a':5, 'b':3, 'c':0, 'd':7},
            'd':{'a':6, 'b':4, 'c':7, 'd':0}}
        G3=copy.deepcopy(G2)
        MST1=DijkstraMSTUndirected(G2)
        MST2=DijkstraMSTUndirectedMatrix(G3)
        print(MST1)
        print(MST2)
        print("-------")
        x,nodes=20,[]
        for ch in range(97,97+x+1): nodes.append(chr(ch))
        G4=GenerateRandomCompleteUndirectedGraph(nodes)
        lc=0
        while lc<100:
            try:
                DijkstraMSTUndirectedMatrix(G4,True)
                break
            except RuntimeError:
                print("Update, step {}".format(lc+1))
                lc=lc+1
        if lc>=100: raise RuntimeError("Cannot generate random graph")
        for u in G4:
            print("{}:{}".format(u,G4[u]))
        G5=copy.deepcopy(G4)
        MST1=DijkstraMSTUndirected(G4)
        MST2=DijkstraMSTUndirectedMatrix(G5)
        for u in MST2:
            print("{}:{}".format(u,MST2[u]))

    def test_EdmondsKarp(self):
        G1={'s1': {'s1':0,'v1':10,'v2':5,'v3':8,'v4':0,'d1':0},
            'v1': {'s1':0,'v1':0,'v2':0,'v3':0,'v4':3,'d1':5},
            'v2': {'s1':0,'v1':0,'v2':0,'v3':0,'v4':3,'d1':10},
            'v3': {'s1':0,'v1':3,'v2':3,'v3':0,'v4':10,'d1':0},
            'v4': {'s1':0,'v1':0,'v2':0,'v3':0,'v4':0,'d1':8},
            'd1': {'s1':0,'v1':0,'v2':0,'v3':0,'v4':0,'d1':0}}
        G2={'a':{'a':0,'b':21,'c':10,'d':0,'e':0,'f':16,'g':0,'h':0,'i':0,'j':0},
            'b':{'a':0,'b':0,'c':0,'d':14,'e':7,'f':0,'g':0,'h':0,'i':0,'j':0},
            'c':{'a':0,'b':0,'c':0,'d':0,'e':0,'f':9,'g':0,'h':0,'i':0,'j':0},
            'd':{'a':0,'b':0,'c':0,'d':0,'e':0,'f':8,'g':25,'h':0,'i':0,'j':0},
            'e':{'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':11,'j':0},
            'f':{'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':13,'i':0,'j':0},
            'g':{'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':14},
            'h':{'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':6,'h':0,'i':0,'j':17},
            'i':{'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':9,'h':0,'i':0,'j':19},
            'j':{'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0}}
        r1=EdmondsKarp(G1,'s1','d1')[0]
        #print(r1)
        r2=EdmondsKarp(G2,'a','j')[0]
        #print(r2)

    def test_EulerianCycles(self):
        G = {}
        G['a'] = {'adj':['b','f']}
        G['b'] = {'adj':['a','c']}
        G['c'] = {'adj':['b','d']}
        G['d'] = {'adj':['c','e']}
        G['e'] = {'adj':['d','f','m','j']}
        G['f'] = {'adj':['a','e','g','k']}
        G['g'] = {'adj':['f','h']}
        G['h'] = {'adj':['g','i']}
        G['i'] = {'adj':['h','j']}
        G['j'] = {'adj':['e','i']}
        G['k'] = {'adj':['f','l']}
        G['l'] = {'adj':['k','m']}
        G['m'] = {'adj':['l','e']}
        G1=copy.deepcopy(G)
        G2=copy.deepcopy(G)
        G3=copy.deepcopy(G)
        isc=IsEulerianCircuit(G1, 'a')
        #print(isc)
        cycle=Fleury(G2,'a')
        #print(cycle)
        cycle=Fleury(G3,'f')
        #print(cycle)
        G4 = {}
        G4['a'] = {'adj':['b','f']}
        G4['b'] = {'adj':['a','c']}
        G4['c'] = {'adj':['b','d']}
        G4['d'] = {'adj':['c','e']}
        G4['e'] = {'adj':['d','f','k','m']}
        G4['f'] = {'adj':['a','e','k','m']}
        G4['g'] = {'adj':['h','l']}
        G4['h'] = {'adj':['g','i']}
        G4['i'] = {'adj':['h','j']}
        G4['j'] = {'adj':['i','k']}
        G4['k'] = {'adj':['e','f','l','j']}
        G4['l'] = {'adj':['g','k']}
        G4['m'] = {'adj':['e','f']}
        G5=copy.deepcopy(G4)
        cycle=Fleury(G4,'m')
        #print(cycle)
        cycle=Hierholzer(G5,'m')
        #print(cycle)
        G= {'A': {'A':0,'B':2,'C':0,'D':2,'E':0,'F':0,'G':0,'H':0},
            'B': {'A':2,'B':0,'C':6,'D':0,'E':7,'F':0,'G':0,'H':0},
            'C': {'A':0,'B':6,'C':0,'D':1,'E':0,'F':3,'G':0,'H':0},
            'D': {'A':1,'B':0,'C':1,'D':0,'E':3,'F':0,'G':0,'H':0},
            'E': {'A':0,'B':7,'C':0,'D':3,'E':0,'F':2,'G':0,'H':12},
            'F': {'A':0,'B':0,'C':3,'D':0,'E':2,'F':0,'G':5,'H':1},
            'G': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':5,'G':0,'H':3},
            'H': {'A':0,'B':0,'C':0,'D':0,'E':12,'F':1,'G':3,'H':0}}
        G6=Eulerization(G)
        cycle=Hierholzer(G6,'b')
        #print(cycle)

    def test_ZI2021_2022(self):
        # G= {'A': {'A':0,'B':4,'C':0,'D':2,'E':0,'F':0,'G':0,'H':0},
        #     'B': {'A':4,'B':0,'C':2,'D':0,'E':3,'F':0,'G':0,'H':0},
        #     'C': {'A':0,'B':2,'C':0,'D':1,'E':0,'F':9,'G':0,'H':0},
        #     'D': {'A':2,'B':0,'C':1,'D':0,'E':9,'F':0,'G':0,'H':0},
        #     'E': {'A':0,'B':3,'C':0,'D':9,'E':0,'F':2,'G':0,'H':4},
        #     'F': {'A':0,'B':0,'C':9,'D':0,'E':2,'F':0,'G':2,'H':10},
        #     'G': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':2,'G':0,'H':1},
        #     'H': {'A':0,'B':0,'C':0,'D':0,'E':4,'F':10,'G':1,'H':0}}
        # G= {'A': {'A':0,'B':2,'C':0,'D':2,'E':0,'F':0,'G':0,'H':0},
        #     'B': {'A':2,'B':0,'C':6,'D':0,'E':7,'F':0,'G':0,'H':0},
        #     'C': {'A':0,'B':6,'C':0,'D':1,'E':0,'F':3,'G':0,'H':0},
        #     'D': {'A':1,'B':0,'C':1,'D':0,'E':3,'F':0,'G':0,'H':0},
        #     'E': {'A':0,'B':7,'C':0,'D':3,'E':0,'F':2,'G':0,'H':12},
        #     'F': {'A':0,'B':0,'C':3,'D':0,'E':2,'F':0,'G':5,'H':1},
        #     'G': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':5,'G':0,'H':3},
        #     'H': {'A':0,'B':0,'C':0,'D':0,'E':12,'F':1,'G':3,'H':0}}
        Zero={'A': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0},
            'B': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0},
            'C': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0},
            'D': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0},
            'E': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0},
            'F': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0},
            'G': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0},
            'H': {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0}}

        # G= {'A': {'A':0,'B':7,'C':0,'D':9,'E':2,'F':0,'G':0,'H':0},
        #     'B': {'A':7,'B':0,'C':8,'D':0,'E':0,'F':1,'G':0,'H':0},
        #     'C': {'A':0,'B':8,'C':0,'D':10,'E':0,'F':0,'G':2,'H':0},
        #     'D': {'A':9,'B':0,'C':10,'D':0,'E':0,'F':0,'G':0,'H':1},
        #     'E': {'A':2,'B':0,'C':0,'D':0,'E':0,'F':1,'G':4,'H':2},
        #     'F': {'A':0,'B':1,'C':0,'D':0,'E':1,'F':0,'G':2,'H':4},
        #     'G': {'A':0,'B':0,'C':2,'D':0,'E':4,'F':2,'G':0,'H':1},
        #     'H': {'A':0,'B':0,'C':0,'D':1,'E':2,'F':4,'G':1,'H':0}}
        # G= {'A': {'A':0,'B':8,'C':0,'D':10,'E':1,'F':0,'G':0,'H':0},
        #     'B': {'A':8,'B':0,'C':9,'D':0,'E':0,'F':1,'G':0,'H':0},
        #     'C': {'A':0,'B':9,'C':0,'D':7,'E':0,'F':0,'G':1,'H':0},
        #     'D': {'A':10,'B':0,'C':7,'D':0,'E':0,'F':0,'G':0,'H':1},
        #     'E': {'A':1,'B':0,'C':0,'D':0,'E':0,'F':4,'G':1,'H':5},
        #     'F': {'A':0,'B':1,'C':0,'D':0,'E':4,'F':0,'G':3,'H':1},
        #     'G': {'A':0,'B':0,'C':1,'D':0,'E':1,'F':3,'G':0,'H':2},
        #     'H': {'A':0,'B':0,'C':0,'D':1,'E':5,'F':1,'G':2,'H':0}}
        # G= {'A': {'A':0,'B':11,'C':0,'D':9,'E':2,'F':0,'G':0,'H':0},
        #     'B': {'A':11,'B':0,'C':13,'D':0,'E':0,'F':3,'G':0,'H':0},
        #     'C': {'A':0,'B':13,'C':0,'D':8,'E':0,'F':0,'G':2,'H':0},
        #     'D': {'A':9,'B':0,'C':8,'D':0,'E':0,'F':0,'G':0,'H':1},
        #     'E': {'A':2,'B':0,'C':0,'D':0,'E':0,'F':9,'G':1,'H':3},
        #     'F': {'A':0,'B':3,'C':0,'D':0,'E':9,'F':0,'G':1,'H':20},
        #     'G': {'A':0,'B':0,'C':2,'D':0,'E':1,'F':1,'G':0,'H':8},
        #     'H': {'A':0,'B':0,'C':0,'D':1,'E':3,'F':20,'G':8,'H':0}}
        # G= {'A': {'A':0,'B':2,'C':0,'D':15,'E':9,'F':0,'G':0,'H':0},
        #     'B': {'A':2,'B':0,'C':11,'D':0,'E':0,'F':12,'G':0,'H':0},
        #     'C': {'A':0,'B':11,'C':0,'D':18,'E':0,'F':0,'G':1,'H':0},
        #     'D': {'A':15,'B':0,'C':18,'D':0,'E':0,'F':0,'G':0,'H':1},
        #     'E': {'A':9,'B':0,'C':0,'D':0,'E':0,'F':8,'G':3,'H':2},
        #     'F': {'A':0,'B':12,'C':0,'D':0,'E':8,'F':0,'G':7,'H':3},
        #     'G': {'A':0,'B':0,'C':1,'D':0,'E':3,'F':7,'G':0,'H':7},
        #     'H': {'A':0,'B':0,'C':0,'D':1,'E':2,'F':3,'G':7,'H':0}}
        G= {'A': {'A':0,'B':12,'C':0,'D':18,'E':1,'F':0,'G':0,'H':0},
            'B': {'A':12,'B':0,'C':10,'D':0,'E':0,'F':1,'G':0,'H':0},
            'C': {'A':0,'B':10,'C':0,'D':1,'E':0,'F':0,'G':12,'H':0},
            'D': {'A':18,'B':0,'C':1,'D':0,'E':0,'F':0,'G':0,'H':9},
            'E': {'A':1,'B':0,'C':0,'D':0,'E':0,'F':13,'G':2,'H':10},
            'F': {'A':0,'B':1,'C':0,'D':0,'E':13,'F':0,'G':10,'H':3},
            'G': {'A':0,'B':0,'C':12,'D':0,'E':2,'F':10,'G':0,'H':2},
            'H': {'A':0,'B':0,'C':0,'D':9,'E':10,'F':3,'G':2,'H':0}}
        G6=Eulerization(G)
        cycle=Hierholzer(G6,'A')
        total=0
        for (u,v) in cycle:
            total+=G[u][v]
        print(total)
        print(cycle)

    def test_FindCycle(self):
        G = {}
        G['a'] = {'adj':['b']}
        G['b'] = {'adj':['c']}
        G['c'] = {'adj':['d','e','f']}
        G['d'] = {'adj':[]}
        G['e'] = {'adj':['b']}
        G['f'] = {'adj':['b']}
        cycs=FindCycles(G)
        #print(cycs)

    def test_Kruskal(self):
        G= {'a': {'a':0,'b':6,'c':5,'d':0,'e':0,'f':0,'g':0},
            'b': {'a':6,'b':0,'c':9,'d':0,'e':13,'f':0,'g':0},
            'c': {'a':5,'b':9,'c':0,'d':16,'e':0,'f':12,'g':0},
            'd': {'a':0,'b':0,'c':16,'d':0,'e':15,'f':7,'g':0},
            'e': {'a':0,'b':13,'c':0,'d':15,'e':0,'f':0,'g':8},
            'f': {'a':0,'b':0,'c':12,'d':7,'e':0,'f':0,'g':3},
            'g': {'a':0,'b':0,'c':0,'d':0,'e':8,'f':3,'g':0}}
        MST=KruskalUndirected(G)
        #print(MST)

    def test_Prim(self):
        G= {'a': {'a':0,'b':6,'c':5,'d':0,'e':0,'f':0,'g':0},
            'b': {'a':6,'b':0,'c':9,'d':0,'e':13,'f':0,'g':0},
            'c': {'a':5,'b':9,'c':0,'d':16,'e':0,'f':12,'g':0},
            'd': {'a':0,'b':0,'c':16,'d':0,'e':15,'f':7,'g':0},
            'e': {'a':0,'b':13,'c':0,'d':15,'e':0,'f':0,'g':8},
            'f': {'a':0,'b':0,'c':12,'d':7,'e':0,'f':0,'g':3},
            'g': {'a':0,'b':0,'c':0,'d':0,'e':8,'f':3,'g':0}}
        MST=Prim(G,'a')
        #print(MST)

    def test_SCCSearch(self):
        G = {}
        G['a'] = {'adj':['c']}
        G['c'] = {'adj':['f']}
        G['f'] = {'adj':['a']}
        G['d'] = {'adj':['a','f','b']}
        G['b'] = {'adj':['e','h']}
        G['e'] = {'adj':['d']}
        G['h'] = {'adj':['g','i','k']}
        G['g'] = {'adj':['b','k']}
        G['k'] = {'adj':[]}
        G['i'] = {'adj':['j']}
        G['j'] = {'adj':[]}
        res=SCCSearch(G)
        #print(res)

    def test_WFI(self):
        G= {'a': {'a':0,'b':0,'c':3,'d':2,'e':0,'f':0,'g':0,'h':0,'i':0},
            'b': {'a':0,'b':0,'c':12,'d':2,'e':1,'f':1,'g':5,'h':0,'i':0},
            'c': {'a':3,'b':12,'c':0,'d':0,'e':0,'f':6,'g':0,'h':0,'i':0},
            'd': {'a':2,'b':2,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0},
            'e': {'a':0,'b':1,'c':0,'d':0,'e':0,'f':0,'g':0,'h':1,'i':0},
            'f': {'a':0,'b':1,'c':6,'d':0,'e':0,'f':0,'g':0,'h':2,'i':1},
            'g': {'a':0,'b':5,'c':0,'d':0,'e':0,'f':0,'g':0,'h':9,'i':2},
            'h': {'a':0,'b':0,'c':0,'d':0,'e':1,'f':2,'g':9,'h':0,'i':0},
            'i': {'a':0,'b':0,'c':0,'d':0,'e':0,'f':1,'g':2,'h':0,'i':0}}
        G={'A': {'A':0,'B':1,'C':2,'D':1,'E':0},
            'B': {'A':0,'B':0,'C':0,'D':0,'E':4},
            'C': {'A':2,'B':0,'C':0,'D':-1,'E':3},
            'D': {'A':0,'B':0,'C':3,'D':0,'E':2},
            'E': {'A':2,'B':-1,'C':0,'D':0,'E':0}}
        #G={'A': {'A':0,'B':7,'C':1,'D':0,'E':1},
        #    'B': {'A':0,'B':0,'C':2,'D':9,'E':0},
        #    'C': {'A':0,'B':0,'C':0,'D':0,'E':2},
        #    'D': {'A':0,'B':5,'C':1,'D':0,'E':0},
        #    'E': {'A':-1,'B':0,'C':0,'D':3,'E':0}}
        (D,P)=WFI(G)
        print(D)
        print(RevWFI(P,'C','B'))
        #print(D['b']['c'])
        #print(D['b']['g'])
        #print(D['b']['h'])
        #print(D['c']['g'])
        #print(D['c']['h'])
        #print(D['g']['h'])
        #print('***')
        #print(RevWFI(P,'b','c'))
        #print(RevWFI(P,'b','g'))
        #print(RevWFI(P,'b','h'))
        #print(RevWFI(P,'c','g'))
        #print(RevWFI(P,'c','h'))
        #print(RevWFI(P,'g','h'))

    def test_WFI2(self):
        #G= {'a': {'a':0,'b':0,'c':4,'d':0,'e':0},
        #    'b': {'a':5,'b':0,'c':0,'d':3,'e':2},
        #    'c': {'a':0,'b':-1,'c':0,'d':11,'e':0},
        #    'd': {'a':7,'b':0,'c':0,'d':0,'e':3},
        #    'e': {'a':1,'b':-2,'c':12,'d':0,'e':0}}
        W={'a':{'a':0, 'b':2, 'c':0, 'd':0},
            'b':{'a':0, 'b':0, 'c':3, 'd':-1},
            'c':{'a':-1, 'b':0, 'c':0, 'd':7},
            'd':{'a':3, 'b':0, 'c':0, 'd':0}}
        (D,P)=WFI(W)
        print(D)
        print(P)
        #print(D['b']['c'])
        #print(D['b']['g'])
        #print(D['b']['h'])
        #print(D['c']['g'])
        #print(D['c']['h'])
        #print(D['g']['h'])
        #print('***')
        print(RevWFI(P,'a','d'))
        #print(RevWFI(P,'b','g'))
        #print(RevWFI(P,'b','h'))
        #print(RevWFI(P,'c','g'))
        #print(RevWFI(P,'c','h'))
        #print(RevWFI(P,'g','h'))

    def test_WFI3(self):
        x,nodes=20,[]
        for ch in range(97,97+x+1): nodes.append(chr(ch))
        s=randint(97,97+x)
        G=GenerateRandomMatrix(nodes,chr(s))
        t=s
        while t==s: t=randint(97,97+x)
        (D,P)=WFI(G)
        print(D)
        print(P)
        print(list(reversed(RevWFI(P,chr(s),chr(t)))))

if __name__ == '__main__':
    unittest.main()
