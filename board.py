class BoardIndexOutOfRangeError(Exception):
    pass

class BoardRevealMineError(Exception):
    pass

loc1 = [(6, 0), (15, 9), (17, 6), (5, 12), (1, 16), (5, 3), (14, 0), (1, 2), (2, 3), (1, 11), (1, 11),
        (14, 12), (3, 7), (12, 1), (1, 16), (15, 8), (7, 16), (16, 17), (6, 1), (13, 12), (8, 7), (8, 9), (2, 7),
        (0, 3), (12, 16), (3, 5), (15, 4), (17, 7), (5, 10), (14, 10), (15, 16), (15, 13), (4, 2), (14, 15), (4, 12),
        (2, 14), (6, 9), (10, 15), (14, 16), (8, 12), (8, 4), (3, 8)]

class Board():
    def __init__(self, size = 18, num_mine = 40, loc = loc1):
        
        mine_loc = loc

        self.__board =  [[None for row in range(size)] for col in range(size)]
        self.size = size
        self.num_mine = num_mine

        for (s, t) in mine_loc:
            self.__board[s][t] = -1

        for i in range(self.size):
            for j in range(self.size):
                if self.__board[i][j] == -1:
                    continue
                count = 0
                for s in range(max(i-1, 0), min(i+2, self.size)):
                    for t in range(max(j-1, 0), min(j+2, self.size)):
                        if s == i and t == j:
                            continue
                        if self.__board[s][t] == -1:
                            count += 1
                self.__board[i][j] = count

    def reveal(self, s, t):
        if s < 0 or s >= self.size or t < 0 or t >= self.size:
            print("The reveal index is out of range")
            raise BoardIndexOutOfRangeError

        r = self.__board[s][t]

        if r == -1:
            print("You've just revealed a mine.")
            raise BoardRevealMineError

        return r

    def collectAll(self, board, to_find = -1):
        collect = []
        for (i, j) in [(i, j) for i in range(self.size) for j in range(self.size)]:
            if board[i][j] == to_find:
                collect.append((i, j))
        return collect


    def evaluate(self, play_board):
        if len(play_board) != self.size:
            print("Inappropriate board size")
            return
        this = set(self.collectAll(self.__board))
        that = set(self.collectAll(play_board))

        print("Correct, Incorrect, Total Reveal: {}, {}, {}".format(len(this & that), len(that - this), 
            324 - len(self.collectAll(play_board, None))))

    def __repr__(self):
        s = list(map(lambda x : list(map(lambda y: f'{y} ' if y != -1 else '* ', x)), self.__board))
        return "\n".join("".join(s[i]) for i in range(self.size))


    def init_playboard(self):
        self.playboard = [[None for i in range(self.size)] for j in range(self.size)]
        return self.playboard

    def get_playboard(self):
        return self.playboard
