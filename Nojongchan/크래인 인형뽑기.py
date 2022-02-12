def solution(board, moves):    
  
    result_box = []
 
    for i in range(len(moves)):
        index = moves[i] - 1
        for j in range(len(board)):
            if board[j][index] != 0:
                result_box.append(board[j][index])
                board[j][index] = 0
                break
  
    original_length =len(result_box)

    def search(box):
      
        for i in range(len(box)-1):
            if box[i] == box[i+1]:
                box.pop(i)
                box.pop(i)
                return search(box)

        changed_length = len(box)
      
        dolls_disappered = original_length - changed_length    
        return dolls_disappered
    
    return search(result_box)
    
  



        


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
