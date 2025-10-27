from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:


        graph = defaultdict(list)

        for ai, bi in edges:
            graph[ai].append(bi)
            graph[bi].append(ai)

        leaves = []
        for idx, value in graph.items():
            if len(value) <= 1:
                leaves.append(idx)
        
        while n > 2:    
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                adj = graph[leaf].pop()
                graph[adj].remove(leaf)

                if len(graph[adj]) == 1:
                    new_leaves.append(adj)
            leaves = new_leaves
        return leaves


        
        
    