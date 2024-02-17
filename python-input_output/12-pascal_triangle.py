def pascal_triangle(n):
    """
    Generates the Pascal's triangle of size n.

    Args:
        n: The number of rows in the Pascal's triangle.

    Returns:
        A list of lists representing the Pascal's triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for row_index in range(1, n):
        row = [1] * (row_index + 1)
        for col_index in range(1, row_index):
            row[col_index] = triangle[row_index - 1][col_index - 1] \
               + triangle[row_index - 1][col_index]
    triangle.append(row)

    return triangle
