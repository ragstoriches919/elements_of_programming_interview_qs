def sudoku(A):

    # Rows
    for row in range(0, len(A)):

        dict_rows = {}

        for col in range(0, len(A[0])):

            # Rows
            if A[row][col] != 0:
                if A[row][col] in dict_rows:
                    return False
                else:
                    dict_rows[A[row][col]] = 1

    # Columns
    for row in range(0, len(A[0])):
        dict_cols = {}

        for col in range(0, len(A[0])):
            if A[col][row] != 0:
                if A[col][row] in dict_cols:
                    return False
                else:
                    dict_cols[A[col][row]] = 1

        print(dict_cols)


    def check_region(row_init, col_init, subA):
        dict_region = {}
        for row in range(row_init, row_init + 3):
            for col in range(col_init, col_init + 3):
                print(row, col)
                if subA[row][col] in dict_region:
                    return False
                else:
                    subA[row][col] = 1

        return True

    check_region(0, 0, A)

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            check_region(row, col, A)


    # Grid



A = [[1, 2, 3, 4, 7, 0, 5, 6, 0], [6, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

sudoku(A)

y = [x**2 for x in range(0, 9)]

