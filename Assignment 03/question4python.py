position = [[0, 0, 0, 0, 0, 0, 2, 0],
                 [0, 0, 0, 2, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 0, 2]]

def valid(m, n):

    if (m >= 0 and m < 8 and n >= 0 and n < 8):
        return True
    return False

def H3():
    answer = 0
    for i in range(8):
        for j in range(8):
            if (position[i][j] == 1):
                for k in range(j + 1, 8):
                    if (position[i][k] == 1):
                        answer = answer + 1
                for k in range(i + 1, 8):
                    if (position[k][j] == 1):
                        answer = answer + 1
                for d in range(1, 8):
                    m = i + d
                    n = j + d
                    if (valid(m, n) and position[m][n] == 1):
                        answer = answer + 1
                    m = i - d
                    n = j + d
                    if (valid(m, n) and position[m][n] == 1):
                        answer = answer + 1
    print('Heuristics 3 :',answer)
H3()
