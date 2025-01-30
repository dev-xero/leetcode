# 

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union-Find with path compression
        N = len(edges)
        parent = [i for i in range(N+1)]
        rank = [1] * (N + 1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # Redundant connection
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for edge in edges:
            n1, n2 = edge[0], edge[1]
            if not union(n1, n2):
                return edge


        return []
