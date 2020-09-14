class Solution:
    def spiralOrder(self, matrix):
        if not matrix[0] or not matrix:
            return []
        rows = len(matrix)
        columns = len(matrix[0])
        total = rows * columns
        order =  [0] * total
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        row = 0
        column = 0
        visited = [[False] * columns for _ in range(rows)] 
        #tmp = [[False] * columns] * rows
        #print(visited)
        #print(tmp)
        #print(tmp==visited)
        visited = tmp
        direction_index = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextrow,nextcolumn = row + directions[direction_index][0] ,column + directions[direction_index][1]
            if not ( 0 <= nextrow < rows and 0 <= nextcolumn < columns and (not visited[nextrow][nextcolumn])):
                direction_index = (direction_index + 1) % 4
            #print(directions[direction_index])
            row = row + directions[direction_index][0]
            column = column + directions[direction_index][1]
            #print(row,column)
        return order
if __name__ == "__main__":
    sl = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = sl.spiralOrder(matrix)
    #print(res)
