from collections import deque as queue

# Function to check if a cell
# is be visited or not


def isValid(vis, row, col, suma):

    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= suma or col >= suma):
        return False

    # If cell is already visited
    if (vis[row][col]):
        return False

    # Otherwise
    return True

# Function to perform the BFS traversal


def BFS(grid, row, col):

    # Stores indices of the matrix cells
    q = queue()

    # Mark the starting cell as visited
    # and push it into the queue
    q.append((row, col))
    grid[col][row] = grid[row][col]

    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end=" ")

        # q.pop()

        # Go to the adjacent cells
        for i in range(suma):
            if()
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(grid, adjx, adjy, suma)):
                q.append((adjx, adjy))
                grid[adjx][adjy] = True


if __name__ == '__main__':

    n = 3
    m = 3
    k = 13
    t = 35
    suma = n+m+k+t+2

    # deklaracja macierzy (0 oznacza brak przeplywu w grafie)
    grid = [[0 for i in range(suma)] for j in range(suma)]

    # wprowadzanie zmiennych do macierzy (Kazik)

    BFS(grid, 0, 0, suma)
