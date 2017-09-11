def optimal_weight(W, w):
    '''(number, list)->number
    Given a capacity of a cargo 'W' and a set of items 'w' with
    different weights. Returns a maximum weight of items that can fit.
    >>>optimal_weight(10,[1,4,8])
    9
    >>>optimal_weight(10,[12, 15])
    0
    '''

    w.insert(0, 0)  # inserts 0 at position 0
    W=int(W)
    matrix = [[0] * (W + 1) for j in range(len(w))]
    for i in range(1, len(w)):
        for j in range(1, W + 1):
            matrix[i][j] = matrix[i - 1][j]
            if w[i] <= j:
                temp = w[i] + matrix[i - 1][j - w[i]]
                if matrix[i][j] < temp:
                    matrix[i][j] = temp
    return matrix[len(w) - 1][W]





