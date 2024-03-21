import sys
from collections import deque
sys.setrecursionlimit(10**6)

def knight_bfs(curr_pos, dest_pos):
  board[curr_pos[0]][curr_pos[1]] = 1
  bfs_queue = deque([curr_pos])
  dx = [2,2,-2,-2,1,1,-1,-1]
  dy = [1,-1,1,-1,2,-2,2,-2]
  
  while bfs_queue:
    v = bfs_queue.popleft()
    if dest_pos[0] == v[0] and dest_pos[1]==v[1]:
      return board[v[0]][v[1]]
    for i in range(8):
      moveX = v[0]+dx[i]
      moveY = v[1]+dy[i]
      if 0<=moveX<size and 0<=moveY<size and board[moveX][moveY]==0:
        board[moveX][moveY]=board[v[0]][v[1]]+1
        bfs_queue.append([moveX,moveY])

for i in range(int(sys.stdin.readline())):
  size = int(sys.stdin.readline())
  board = [[0 for i in range(size)] for i in range(size)]
  curr_pos = list(map(int,sys.stdin.readline().split()))
  dest_pos = list(map(int,sys.stdin.readline().split()))

  cnt = knight_bfs(curr_pos,dest_pos)
  print(cnt-1)
  

  
          
          