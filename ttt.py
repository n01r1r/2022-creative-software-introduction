print("학번: 202020778, 이름: 한동엽")


def isRightFile(filename):
    lines = []
    comm = []  # command list
    check = []
    board = ["", "", "", "", "", "", "", "", ""]  # 3x3 board
    i = 0
    c = 0

    f = open(filename, "r")
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        line = line.split(", ")
        lines.append(line)
    f.close()

    while i < len(lines):
        comm.extend(lines[i])
        i = i + 1
    length = int(len(comm) / 3)

    while c < length:  # 각 자리에 알맞은 형태인지 확인
        a = int(comm[c * 3 + 1])
        b = int(comm[c * 3 + 2])
        if type(a) == int and type(b) == int and 0 < a < 4 and 0 < b < 4:  # 정수, 범위 확인
            index = 3 * (a - 1) + (b - 1)
            value = str(comm[c * 3])
        else:
            return "-"

        if value != "O" and value != "X":  # OX 문자, 범위 확인
            return "-"

        board[index] = value
        check.append(value)

        if 1 < c < length:  # 교대 확인, 앞뒤로 같으면 break
            if check[c - 1] != check[c]:
                pass
            else:
                return "-"

        c = c + 1

    return board


def getWinner(filename):
    if (
        isRightFile(filename) != "-" and len(isRightFile(filename)) >= 5
    ):  # 승자 판별되는 경우만 분류
        res = isRightFile(filename)

        if res[0] == res[1] == res[2]:
            return res[0]
        elif res[3] == res[4] == res[5]:
            return res[3]
        elif res[6] == res[7] == res[8]:
            return res[6]
        elif res[0] == res[3] == res[6]:
            return res[0]
        elif res[1] == res[4] == res[7]:
            return res[1]
        elif res[2] == res[5] == res[8]:
            return res[2]
        elif res[0] == res[4] == res[8]:
            return res[0]
        elif res[2] == res[4] == res[6]:
            return res[2]
        else:
            return "-"
    else:
        return "-"


print(getWinner("tic-tac-toe-1.txt"))
