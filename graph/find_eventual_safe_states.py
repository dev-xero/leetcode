# https://leetcode.com/problems/find-eventual-safe-states

"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1
        
        q = deque()

        # push all nodes with indegree = 0, into the queue.
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        safeNodes = []
        
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)
    
        return safeNodes
        