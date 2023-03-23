#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    triangle = [[1], [1, 1]]
    for p in range(2, n):
        row = [1]
        for i in range(p-1):
            row.append(triangle[p-1][i] + triangle[p-1][i+1])
        row.append(1)
        triangle.append(row)
    return triangle