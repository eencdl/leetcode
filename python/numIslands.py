__author__ = 'don'

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    # Once you find a '1' set all its neighbours to '2' via dfs
    # then only count the '1'
     def numIslands(self, grid):
         if not grid:
             return 0

         m = len(grid)
         n = len(grid[0])
         cnt = 0
         for y in range(m):
             for x in range(n):
                 if grid[y][x] == '1':
                     self.DFS(grid, x, y, m, n)
                     cnt +=1
         return cnt

     def DFS(self, grid, x, y, m, n):
         if y >= m or x >= n or x < 0 or y < 0:
             return

         if grid[y][x] == '1':
             #represent visited
             #4 neighbours, sometime it maybe 8
             grid[y][x] = '2'
             self.DFS(grid, x-1, y, m, n)
             self.DFS(grid, x, y-1, m, n)
             self.DFS(grid, x+1, y, m, n)
             self.DFS(grid, x, y+1, m, n)
         return


