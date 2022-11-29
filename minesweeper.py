from board import Board
"""
minesweeper.py에 있는 코드는 여러분이 자유롭게 수정하여 사용할 수 있습니다.
find_mines() 합수는 반드시 있어야하는 함수입니다. 없으면, 평가되지 않습니다. 
매개변수도 수정하면 안됩니다.

나머지 함수들은 여러분이 사용할 수 있도록, 미리 만들어 놓았습니다. 
여러분의 지뢰찾는 방식에 따라, 수정하여 사용할 수 있습니다.

"""


def collectWindow(board, i, j, to_find=-1, size=18):
  """
    (i, j) 격자 (Cell) 주변의 to_find 값을 가지는 격자를 모읍니다.
    """
  collect = []
  for s in range(max(i - 1, 0), min(i + 2, size)):
    for t in range(max(j - 1, 0), min(j + 2, size)):
      if board[s][t] == to_find:
        collect.append((s, t))
  return collect


def printBoard(board, size):
  s = list(
    map(
      lambda x: list(
        map(
          lambda y: '* ' if y == -1 else '? ' if y == None else '  '
          if y == 0 else f'{y} ', x)), board))
  print("")
  print("\n".join("".join(s[i]) for i in range(size)))
  print("-" * 50)
  print("")
  return


def reveal(board, s, t):
  """
    (s,t)위치의 격자를 엽니다. (reveal)
    지뢰가 없다면, 주변의 지뢰가 몇개가 있는지 알려줍니다.
    만약 지뢰가 있는 위치를 열었다면, 게임이 종료됩니다. (Game Over)
    """

  global gameBoard
  v = gameBoard.reveal(s, t)
  board[s][t] = v
  print('{}, {} revealed'.format(s, t))
  return v


def mark(board, s, t):
  """
    (s, t) 위치의 격자에 지뢰가 있을 것이라고 표시합니다.
    """
  board[s][t] = -1
  print('{}, {} marked'.format(s, t))
  return


def reveal_zeros(board, i, j, size=18):
  """
    (i, j) 위치의 격자를 밝히고 그 격자 주변에 지뢰가 없다는 것이 밝혀지면,
    그 위치부터 시작하여, 최대한 넓게 격자들을 밝혀냅니다.
    더 좋게 개선할 수 있는 코드입니다.
    """
  if i < 0 or j < 0 or i >= size or j >= size:
    return

  v = reveal(board, i, j)
  if v != 0:
    return

  for s in range(max(0, i - 1), min(size, i + 2)):
    for t in range(max(0, j - 1), min(size, j + 2)):
      if s == i and t == j:
        continue
      if board[s][t] != None:
        continue
      v = reveal(board, s, t)
      if v == 0:
        reveal_zeros(board, s, t)


def auto_reveal(board, base=1, size=18):
  print("Starting auto_reveal...")
  count = 0  # count reveal or mark
  for (i, j) in [(i, j) for i in range(size) for j in range(size)]:
    if board[i][j] != base:
      continue
    mines = collectWindow(board, i, j, -1)  #먼저 주변에 밝혀진 지뢰찾기
    #print(mines)
    #print("mines printed\n")
    num = len(mines)
    if num == base: #mines=[(s,t)], num=1
      #print("num = 1\n")
      unknowns = collectWindow(board, i, j, None)
      for (s, t) in unknowns:
        count += 1
        v = reveal(board, s, t)
        if v == 0:
          reveal_zeros(board, s, t)
    elif num > base:
      print("Something Wrong")
      return 0
    elif num < base: #mines=[], num=0
      unknowns = collectWindow(board, i, j, None)
      if len(unknowns) + num == base:
        for (s, t) in unknowns:
          mark(board, s, t)
          count += 1
  return count


def findAgain(board, val=3, size=18):
    cnt = 0
    for (i, j) in [(i, j) for i in range(size) for j in range(size)]:
        lists = collectWindow(board, i, j, val)
        for (s,t) in lists:
        #주변 ? 1개인 것부터 처리
            unknown = collectWindow(board, s, t, None)
            mine = collectWindow(board, s, t, -1)
            if len(unknown) == 1: #? 1개, k 중심 k-1개의 지뢰일 경우
                if len(mine) == val-1:
                    print(unknown)
                    print("is a mine\n")
                    mark(board, unknown[0][0], unknown[0][1])
                    cnt += 1
            else:
                pass

            if val == len(mine): #?이 확실하게 지뢰가 아닌 경우
                for a, b in unknown:
                    reveal(board, a, b)
                    cnt += 1
    return cnt
    
def guessMine(board, size=18):
    #정공법으로 안되는 경우
        pass

        
    #return something           
                    
                    #(i,j) 주변 (s,t) 8 지점에 대해서 list로 처리
                    #(s,t)에 대해서 *과 1~3이 적절한 위치인 경우에 대해 언노운 *로 처리
                    # case 1. 언노운 1개
                    #case 1-1. 최고값 k를 중심으로 지뢰가 k-1개 있는 경우 언노운은 지뢰

                    #case 2. 최고값 k를 중심으로 지뢰가 k개 있는 경우 언노운은 지뢰 X (언노운 개수 상관 X)

                    #추정: 2,3, 등 높은 값들 주변의 모든 언노운에 cnt +1
                    #추정: 언노운 중 가장 cnt 높은 것들 mark
                    


def find_mines(board, size=18):
    while auto_reveal(board, 1) > 0:
        num = 8
        while num > 1:
            findAgain(board, num)
            print(num, "-th findAgain")
            num -= 1
        if auto_reveal(board, 1) == 0:
            break
        else:
            continue
    printBoard(board, size)

if __name__ == "__main__":
    gameBoard = Board()
    board = gameBoard.init_playboard()
    print("board printed\n")

    # (11, 10)의 위치 주변에는 지뢰가 없는 것으로 설정되어 있습니다.
    # (11, 10)의 위치에서 아래 처럼 reveal_zero를 먼저 실행하면 좋습니다.
    #
    if reveal(board, 11, 10) == 0:
        reveal_zeros(board, 11, 10)
    findAgain(board)
    # printBoard(board, 18)
    print("\n========================\n")

    find_mines(board) #auto_reveal

    #print(gameBoard.__board)
    gameBoard.evaluate(board)
