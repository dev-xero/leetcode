# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups

"""
You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

    Each node in the graph belongs to exactly one group.
    For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.

Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.
"""


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency-matrix
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Find all connected components
        visited = [False] * (n+1)
        components = []
        for i in range(1, n+1):
            if not visited[i]:
                q = deque([i])
                visited[i] = True
                component = []

                while q:
                    current = q.popleft()
                    component.append(current)

                    for neighbor in adj[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)

                components.append(component)

        # Check if each component if bi-partite
        color = [0] * (n+1)
        for comp in components:
            start = comp[0]
            q = deque([start])

            color[start] = 1
            is_bipartite = True

            while q and is_bipartite:
                current = q.popleft()
                for neighbor in adj[current]:
                    if not color[neighbor]:
                        color[neighbor] = -color[current]
                        q.append(neighbor)

                    elif color[neighbor] == color[current]:
                        is_bipartite = False
                        break

                if not is_bipartite:
                    break

            if not is_bipartite:
                return -1

        # Calculate max number of groups
        total_groups = 0
        for comp in components:
            max_diameter = 0
            # Compute max distance using BFS
            for node in comp:
                distance = {n: -1 for n in comp}
                q = deque([node])
                distance[node] = 0
                current_max = 0

                while q:
                    current = q.popleft()
                    for neighbor in adj[current]:
                        if distance[neighbor] == -1:
                            distance[neighbor] = distance[current] + 1
                            current_max = max(current_max, distance[neighbor])
                            q.append(neighbor)

                if current_max > max_diameter:
                    max_diameter = current_max

            total_groups += max_diameter + 1

        return total_groups
