



class Tester:

    
    @staticmethod
    def subsets(n):
        "Generate all subsets of a set of n elements"

        def search(k: int, curr_set: list[int]):
            if k == n+1:
                # process subset
                ans.append(list(curr_set))
            else:
                curr_set.append(k)
                search(k+1, curr_set)
                curr_set.pop()
                search(k+1, curr_set)
                
        ans = []
        search(1, [])
        return ans

    @staticmethod
    def subset_iter(xs):
        "Generate all subsets from the elements in xs"

        def search(index: int, curr_set):
            if index == len(xs):
                ans.append(list(curr_set))
            else:
                curr_set.append(xs[index])
                search(index+1, curr_set)
                curr_set.pop()
                search(index+1, curr_set)

        ans = []
        search(0, [])
        return ans

    @staticmethod
    def permutations(n):
        "Generate all permutations of a set of 1 to n"

        def search(perm):
            if len(perm) == n:
                ans.append(list(perm))
            else:
                for i in range(1, n+1):
                    if chosen[i]:
                        continue
                    chosen[i] = True
                    perm.append(i)
                    search(perm)
                    chosen[i] = False
                    perm.pop()
        chosen = [False] * (n+1)
        ans = []
        search([])
        return ans


    @staticmethod
    def nqueens(n):
        "Generate a solution to n queens"

        col = [False] * n
        diag = [False] * (2*n+1)
        anti_diag = [False] * (2*n+1)

        def search(row: int):
            nonlocal count
            if row == n:
                count += 1
                return
            # try all column, if the column intersects then invalid, to check if intercept need to store previous queen col, diagonal and anti-diagonal
            for c in range(n):
                if col[c] or diag[c+row] or anti_diag[c+n-row+1]:
                    continue
                col[c] = diag[c+row] = anti_diag[c+n-row+1] = True
                search(row+1)
                col[c] = diag[c+row] = anti_diag[c+n-row+1] = False
        count = 0
        search(0)
        return count

    @staticmethod
    def nqueen_sol(n: int):
        "Print coordinates for the n-queen position"

        col = [False] * n
        diag = [False] * (2*n+1)
        anti_diag = [False] * (2*n+1)

        def search(row: int, solution):
            nonlocal count
            if row == n:
                count += 1
                solutions.append(list(solution))
                return
            # try all column, if the column intersects then invalid, to check if intercept need to store previous queen col, diagonal and anti-diagonal
            for c in range(n):
                if col[c] or diag[c+row] or anti_diag[c+n-row+1]:
                    continue
                col[c] = diag[c+row] = anti_diag[c+n-row+1] = True
                solution.append((row, c))
                search(row+1, solution)
                solution.pop()
                col[c] = diag[c+row] = anti_diag[c+n-row+1] = False
        count = 0
        solutions = []
        search(0, [])
        return solutions



test = Tester()
# print(test.subsets(3))
# 
# print(test.subset_iter("ABCDEFG"))
# 
# print(test.permutations(4))
# 
# print(test.nqueens(8))
# 
# print(test.nqueen_sol(8))




class DPTester:


    @staticmethod
    def LIS(nums):
        "Return longest increasing subsequence"
        def helper(i: int, prev: int):
            # base case is when i reaches end of array
            if i == len(nums):
                return 0
            # at current index of string, we can include it or don't include in subsequence
            # if we don't include, then continue
            exclude_i = helper(i+1, prev)
            include_i = 0
            if nums[i] > prev:
                include_i = helper(i+1, nums[i]) + 1
            return max(exclude_i, include_i)

        return helper(0, float('-inf'))


dptest = DPTester()

test = [6,2,5,1,7,4,8,3]
print(dptest.LIS(test))



class GraphTester:


    @staticmethod
    def dfs(edges:list[tuple[int, int]], N: int):
        # create adjacency list
        adj_list = [[] for _ in range(N)]
        for u, v in edges:
            adj_list[u-1].append(v-1)
        print(adj_list)

        def helper(i: int):
            if visited[i]:
                return
            visited[i] = True
            for v in adj_list[i]:
                helper(v)
            print(i+1)

        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                helper(i)

    @staticmethod
    def bfs(edges:list[tuple[int, int]], N: int):
        adj_list = [[] for _ in range(N)]
        distance = [0] * N
        visited = [False]* N
        for u, v in edges:
            adj_list[u-1].append(v-1)
        visited[0] = True
        distance[0] = 0 
        from collections import deque
        q = deque([0])
        print(adj_list)
        while q:
            s = q.popleft()
            print(s)
            for u in adj_list[s]:
                if visited[u]:
                    continue
                visited[u] = True
                distance[u] = 1 + distance[s]
                q.append(u)
        print(distance)

    @staticmethod
    def bellmanford(edges:list[tuple[int, int, int]], N:int) -> list[int]:
        distance = [float('inf')] * N
        distance[0] = 0
        for i in range(N-1):
            for u, v, weight in edges:
                distance[v] = min(distance[v], distance[u]+weight)
        return distance

    @staticmethod
    def dijkstra(edges:list[tuple[int, int, int]], N: int)-> list[int]:
        adj_list = [[] for _ in range(N)]
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))

        distance = [float('inf')] * N
        visited = [False] * N
        distance[0] = 0
        print(adj_list)
        import heapq
        min_heap = [(0, 0)] # distance, node
        while min_heap:
            _, s = heapq.heappop(min_heap)
            if visited[s]:
                continue
            visited[s] = True
            for u, w in adj_list[s]:
                if distance[s]+w < distance[u]:
                    distance[u] = distance[s]+w
                    heapq.heappush(min_heap, (distance[u], u))
        return distance

    @staticmethod
    def topological_sort(edges:list[tuple[int, int]], N:int) -> None:

        adj_list = [[] for _ in range(N)]
        for u, v in edges:
            adj_list[u].append(v)

        states = [0]*N # 0 = not processed, 1 = processing, 2 = processed

        def dfs(s: int):
            if states[s] == 1:
                # detect cycle
                print("cycle")
                return
            elif states[s] == 2:
                # visited
                return
            states[s] = 1
            for v in adj_list[s]:
                dfs(v)
            states[s] = 2
            topo_list.append(s)
        
        topo_list = []
        for i in range(N):
            if not states[i]:
                dfs(i)
        return list(reversed(topo_list))

            

graphtest = GraphTester()

edges = [[1, 2],
         [1, 4],
         [2, 3],
         [2, 5],
         [5, 3]]

# print(graphtest.dfs(edges, 5))

print(graphtest.bfs(edges, 5))

weighted_edges = [[0, 1, 2],
                  [0, 2, 1],
                  [0, 3, 7],
                  [2, 3, 3],
                  [3, 1, 3],
                  [3, 4, 2],
                  [2, 4, 5]]

print(graphtest.bellmanford(weighted_edges, 5))


weighted_edges2 = [[0, 4, 1],
                   [0, 3, 9],
                   [0, 1, 5],
                   [1, 2, 2],
                   [2, 3, 6],
                   [3, 4, 2]]

print(graphtest.dijkstra(weighted_edges2, 5))


edges2 = [[0, 1],
          [1, 2],
          [2, 5],
          [3, 0],
          [3, 4],
          [4, 1],
          [2, 4]]


print(graphtest.topological_sort(edges2, 6))
