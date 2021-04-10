def solution(board):
    x=len(board)
    y=len(board[0])
    for i in range(x):
        for j in range(y):
            if i==0 or j==0:
                continue
            if board[i][j]!=0:
                board[i][j]=min(board[i-1][j-1],min(board[i-1][j],board[i][j-1]))+1
    answer=[]
    for i in range(row):
        answer.append(max(board[i]))
    return max(answer)**2
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))