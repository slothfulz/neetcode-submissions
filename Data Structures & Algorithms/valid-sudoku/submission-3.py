class Solution:
    '''
    1. 
    understand
    input: lists that contains sublists 
    output: boolean
    edge cases: empty list(True), strings(False)
    logic: 
    row ==> accessed by indexes(0-9)
    column  ==> ex. column 1 [rows 0-9][0]
    3x3 ===> first row of three by threes [row0 -9][column0-2 ]

    2. plan

    1. create a dict variable
    2. nested forloop through each sublist. if n is an int: if n is already in dict return False else add it to dict
    3. for i in range (0,10), for i in range 0,10 
    
    implement
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        threebai= defaultdict(set)
        for i in range(0,9):
            for y in range (0,9):
                if board[i][y] == ".":
                    continue
                if board[i][y] in rows[i] or board[i][y] in cols[y] or board[i][y] in threebai[i//3, y//3]:
                    return False
                else:
                    threebai[i//3, y//3].add(board[i][y])
                    rows[i].add(board[i][y])
                    cols[y].add(board[i][y])
        return True
   
        