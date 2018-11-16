

def print_mat(mat):
    for row in mat:
        print(row)


def rotate_matrix(mat):
    n = len(mat)

    for layer in range(n//2):
        for offset in range(n-1-2*layer):
            tmp                                 = mat[layer][layer+offset]
            mat[layer][layer+offset]            = mat[n-1-layer-offset][layer]
            mat[n-1-layer-offset][layer]        = mat[n-1-layer][n-1-layer-offset]
            mat[n-1-layer][n-1-layer-offset]    = mat[layer+offset][n-1-layer]
            mat[layer+offset][n-1-layer]        = tmp

    return mat



mat = [
    [ 0, 1, 2, 3],
    [ 4, 5, 6, 7],
    [ 8, 9,10,11],
    [12,13,14,15],
]

print_mat(rotate_matrix(mat))
