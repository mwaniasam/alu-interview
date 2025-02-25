#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Parameters:
    n (int): The number of rows in Pascal's triangle.

    Returns:
    list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]
        
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])
        
        current_row.append(1)
        triangle.append(current_row)
    
    return triangle


if __name__ == "__main__":
    # Example usage
    print(pascal_triangle(5))
